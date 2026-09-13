# Design Pattern Examples — Embedded C++ Context

Each example builds on the `TemperatureSensor` interface style you already
have. Interviewers want to see that you can name the pattern *and* give a
concrete embedded/medical use case — not just textbook definitions.

---

## 1. Strategy — swap algorithms behind one interface

Use case: switching filtering or calibration strategy at runtime without
touching the caller.

```cpp
class FilterStrategy
{
public:
    virtual float apply(float rawSample) = 0;
    virtual ~FilterStrategy() = default;
};

class MovingAverageFilter : public FilterStrategy
{
public:
    float apply(float rawSample) override
    {
        buffer_[index_] = rawSample;
        index_ = (index_ + 1) % buffer_.size();
        float sum = 0.0f;
        for (float v : buffer_) sum += v;
        return sum / buffer_.size();
    }
private:
    std::array<float, 8> buffer_{};
    size_t index_ = 0;
};

class NoOpFilter : public FilterStrategy
{
public:
    float apply(float rawSample) override { return rawSample; }
};

class TemperatureChannel
{
public:
    explicit TemperatureChannel(FilterStrategy& filter) : filter_(filter) {}
    float readFiltered(float raw) { return filter_.apply(raw); }
private:
    FilterStrategy& filter_;
};
```

**Talking point:** at Cyden, an IPL device might need a different filtering
strategy for a calibration pass vs normal operation — Strategy lets you swap
that without branching logic scattered through the control code.

---

## 2. Factory — pick the correct driver at startup

Use case: build the right sensor implementation depending on board revision
or compile-time configuration, so the rest of the code only ever sees
`TemperatureSensor&`.

```cpp
enum class BoardVariant { RevA_Adc, RevB_I2c };

std::unique_ptr<TemperatureSensor> createTemperatureSensor(BoardVariant variant)
{
    switch (variant)
    {
        case BoardVariant::RevA_Adc:
            return std::make_unique<AdcTemperatureSensor>();
        case BoardVariant::RevB_I2c:
            return std::make_unique<I2cTemperatureSensor>();
    }
    return nullptr; // unreachable if enum is exhaustive — flag in review
}
```

**Talking point:** board bring-up often means the same firmware image has to
support two hardware revisions during a transition period. A factory keeps
that decision in one place instead of `#ifdef`s spread across the codebase.

---

## 3. Observer / pub-sub — fault and alarm propagation

Use case: multiple modules (logging, UI, safety monitor) need to react when
a sensor reports an out-of-range or fault condition, without the sensor
knowing who's listening.

```cpp
class FaultObserver
{
public:
    virtual void onFault(int faultCode) = 0;
    virtual ~FaultObserver() = default;
};

class FaultPublisher
{
public:
    void subscribe(FaultObserver& observer) { observers_.push_back(&observer); }
    void notifyFault(int faultCode)
    {
        for (auto* obs : observers_) obs->onFault(faultCode);
    }
private:
    std::vector<FaultObserver*> observers_;
};

class SafetyMonitor : public FaultObserver
{
public:
    void onFault(int faultCode) override
    {
        // trigger shutdown, latch alarm state, etc.
    }
};
```

**Talking point:** on a medical device, a single overtemperature fault might
need to simultaneously halt treatment, log the event for regulatory
traceability, and update the UI — Observer decouples "who reacts" from "who
detects."

---

## 4. Facade — simple API over a complex stack

Use case: hide RTOS primitives, DMA setup, and interrupt handling behind a
small, testable interface that application code actually calls.

```cpp
class UartFacade
{
public:
    void init() { /* configure clocks, DMA, IRQ priority, RTOS queue */ }
    void send(std::span<const uint8_t> data) { /* kick off DMA TX */ }
    std::optional<std::vector<uint8_t>> receive(uint32_t timeoutMs)
    {
        // wait on RTOS queue, return data or nullopt on timeout
        return std::nullopt;
    }
};
```

**Talking point:** this is exactly what you'd want reviewable in a
safety-conscious codebase — the facade is the thing a reviewer or test can
reason about, while DMA/IRQ complexity stays contained and doesn't leak into
application logic.

---

## 5. Singleton — single hardware resource, used carefully

Use case: representing genuinely singular hardware (e.g. the one and only
RTC peripheral on the chip) — but flag the testing trade-off unprompted,
since that's what separates a junior answer from a senior one.

```cpp
class SystemClock
{
public:
    static SystemClock& instance()
    {
        static SystemClock inst;
        return inst;
    }
    uint32_t nowMs() const { /* read hardware timer */ return 0; }

    SystemClock(const SystemClock&) = delete;
    SystemClock& operator=(const SystemClock&) = delete;
private:
    SystemClock() = default;
};
```

**Talking point (say this unprompted — it shows seniority):**
> "I'd use Singleton sparingly — it genuinely fits a single hardware
> peripheral, but it makes unit testing harder because you can't easily
> substitute a fake. Where possible I'd prefer passing a reference to the
> resource through the constructor instead, so tests can inject a mock and
> production code injects the real singleton."

---

## How to use this in an interview

If asked "tell me about a design pattern you've used" — pick **one** of
these, describe the *problem* first (in 1-2 sentences), then the pattern,
then a one-line trade-off. Don't lead with the pattern name; interviewers
want to see you recognise the problem shape before reaching for the
solution.
