# Amazon Interview Prep

## Coding-practice provenance

- The Sept 27 embedded coding practice topics were selected from a Glassdoor
  summary of reported Amazon interview themes.
- Treat that summary as candidate-reported practice guidance, not an official
  or guaranteed Amazon question bank.
- The reusable technical conclusions live in the canonical C++, DSA, linked
  list, circular-buffer, and RTOS notes rather than being duplicated here.

## Amazon Behavioural Rounds

### Story: Medical-device software mitigation after diode change

**Best for:** Have Backbone; Disagree and Commit, Dive Deep, Earn Trust,
Ownership, Deliver Results

#### Situation

- Production medical-device product showed intermittent false transitions from
contact to no-contact.
- Device was still visibly in contact with the skin.
- Root cause was traced to increased signal noise after a diode/component
change.
- Hardware change would have meant costly rework/recall-style handling for
affected units.

#### Task

- Find a software mitigation that could be released quickly and reliably.
- Fix still had to pass verification testing and support regulated paperwork /
FDA deviation expectations.
- Goal: eliminate false contact transitions without compromising safety or
validation.

#### Disagreement

- Senior engineer suggestion: reject noisy raw-buffer samples if they fell
outside an expected range.
- My concern: this may treat the symptom without fully understanding how the
noise caused the contact-tracking failure.
- My suggestion: characterise the signal behaviour and adjust closer to the
source of the false transition, not only at the raw buffer.

#### Action

- Compared both approaches through test data, reliability, speed of release,
and ease of verification.
- Discussed trade-offs without making it about who was right.
- Combined the useful parts of both ideas:
  - improve the underlying contact-tracking behaviour;
  - protect against clearly invalid/noisy raw data.

#### Result

- Software fix passed verification testing.
- Eliminated the false contact transitions.
- Went into production.
- Avoided the hardware change for affected units.
- Later production batches no longer showed the same issue.

#### Key Takeaway

- I disagreed constructively, used evidence, and committed to the best combined
solution.
- The decision balanced technical correctness, safety, validation speed, and
production impact.

#### Leadership Principle Mapping

- **Have Backbone; Disagree and Commit:** challenged the raw-buffer-only fix
because I believed it did not fully address the failure mechanism; committed
once the combined approach was agreed.
- **Dive Deep:** looked beyond the symptom and focused on how signal noise was
affecting the contact-tracking logic.
- **Earn Trust:** kept the discussion evidence-based and collaborative with the
senior engineer.
- **Ownership:** treated the issue as a production and customer/user-impact
problem, not just a code change.
- **Deliver Results:** fix passed verification, removed the false transitions,
entered production, and avoided hardware rework for affected units.

#### Likely Follow-up Questions

- What evidence convinced the team to combine both approaches?
- How did you make sure the software fix was safe and not just masking the
problem?
- What trade-offs did you consider between speed, validation, and reliability?
- How did you handle disagreeing with someone more senior?
- What would you do differently if the same issue happened again?
- How did you know later batches no longer had the same issue?

A recent example was on a production medical-device project. We had an issue where the device was being used on skin, 
but it would intermittently switch from “contact” to “no contact” even though it was still physically touching the skin.
We investigated the issue and traced it back to increased signal noise caused by a diode change from the supplier. 
One option was to resolve it through a hardware change, but that would have been expensive and disruptive for affected units,
so we looked for a software mitigation that could still pass our verification process.

The disagreement was around where to fix the problem. A senior engineer suggested filtering the issue at the raw-buffer 
level by rejecting noisy samples. I agreed that raw-data protection was useful, but my concern was that this alone might only
treat the symptom. I wanted us to also understand how the noise was creating the false transition in the contact-tracking 
logic, and handle it closer to where the contact-to-no-contact decision was being made.

We reviewed the data together and compared both approaches in terms of reliability, speed of implementation, and verification 
risk. In the end, we combined both ideas: we rejected clearly invalid noisy raw data, and we also improved the transition 
logic so longer noise events would not incorrectly present as loss of contact to the user.

The software fix passed verification testing, eliminated the false contact transitions, went into production, and avoided
the hardware change for the affected units. Later batches no longer showed the same issue. The main thing I learned was
that disagreement is productive when it stays evidence-based and focused on the safest outcome, not on whose idea wins.

Production issue → diode noise → senior wanted raw-buffer filter → you pushed for transition-logic fix too → data showed
both were needed → passed verification and went to production

### Story: Field-device recovery tool for corrupted configuration

**Best for:** Ownership, Dive Deep, Deliver Results, Customer Obsession, Bias
for Action

#### Situation

- Field devices were returning with corrupted configuration.
- The normal path would have required returns or engineer intervention.
- Warehouse operators needed a safe way to recover affected devices locally.

#### Task

- I volunteered outside my normal scope to adapt an existing handset into a
protected recovery/reprogramming tool.
- The tool needed to be safe for non-engineer operators and prevent accidental
damage to good devices.

#### Action

- Constrained the approved configuration items and values in firmware.
- Added a simple pass/fail UI and an operator instruction sheet.
- Implemented a write/verify sequence.
- Allowed up to three retries, then moved to a safe failure animation rather
than continuing indefinitely.
- Validated the flow with unit, integration, and device-level testing.

#### Result

- Warehouses had a scalable local recovery path.
- The fix reduced dependency on returns or engineer intervention.
- The recovery process was bounded, repeatable, and safer for untrained
operators.

#### Leadership Principle Mapping

- **Ownership:** took responsibility beyond normal role boundaries.
- **Dive Deep:** understood the corrupted configuration and safe value limits.
- **Deliver Results:** produced a practical recovery process operators could use.
- **Customer Obsession / Bias for Action:** reduced delay and friction for
affected devices without waiting for a slower support path.

#### Likely Follow-up Questions

- How did you prevent untrained operators from damaging good devices?
  - Constrain the tool to approved configuration fields and fixed known-good
    values; do not expose arbitrary memory writes or editable values.
  - Validate under-length, over-length, unexpected reply, timeout, and wrong
    state-machine sequencing cases.
  - Compare before/after data so only the expected byte positions change.
  - Fail safely with a documented error/retry state if any step does not
    complete inside the expected time.
- What values were operators allowed to change, and why?
  - Operators did not choose values. The values were fixed in the recovery
    firmware and had already been tested on development units against the
    noisy treatment condition that caused the incorrect contact/no-contact
    state transition.
- How did the write/verify step work?
  - The tool performed the approved write, read back or otherwise verified the
    configured fields, and only showed success when the written data matched
    the expected values.
- What happened after three failed retries?
  - The tool stopped the sequence and displayed the documented fault state
    rather than continuing indefinitely or leaving the operator to guess.
- How did you validate the tool before giving it to warehouses?
  - Separate the validation into two questions: first, prove the configuration
    values solved the original noisy-condition behaviour on the bench; second,
    prove the recovery tool applied those known-good values reliably.
- Why not push a full software release immediately?
  - A full software release would have required implementation, regression
    testing, validation, release activity, and potentially reworking stock that
    was already close to market. The recovery tool was a narrow containment
    path for affected stock; the normal release train remained the correct path
    for a permanent software improvement.
- What would you do differently with more time?
  - Raise the formal software change and take it through the normal release
    process, so the software itself becomes more robust to the noise condition
    rather than relying only on revised configuration limits.

One-line recall:

Corrupted field configuration → volunteered to adapt handset → constrained
approved values → pass/fail UI + instructions → write/verify + three retries
then safe fail → local warehouse recovery. Short-term containment was the
bounded recovery tool; long-term corrective action would be a software fix
through the release train.

### Story: Production unlock failures halting factory throughput

**Best for:** Bias for Action, Dive Deep, Ownership, Deliver Results

#### Situation

- I maintained software on a production PCB used to configure and calibrate
devices during manufacturing.
- Factory runs started failing during the device unlock sequence.
- Devices would stop progressing and throughput was affected.
- At first it was unclear whether the root cause was the device, PCB, or
communication sequence.

#### Task

- Identify the failure quickly under production time pressure.
- Restore reliable unlock flow without only patching the visible symptom.

#### Action

- Reviewed logs and broke the unlock sequence into stages.
- Isolated where communication stopped and reproduced the failure under
controlled conditions.
- Traced the issue to stale message-buffer state from the previous transaction.
- Found the buffer-in-use flag handling was not correctly marking/freeing buffer
state for the next device.
- Fixed the flag handling.
- Added explicit communication-buffer reinitialisation at the start of each
new-device unlock sequence so every transaction begins from a known clean
state.

#### Result

- Production unlock flow became reliable again.
- The prevention was more robust than only fixing one stale flag, because a new
device no longer inherited communication state from the previous device.

#### Leadership Principle Mapping

- **Bias for Action:** moved quickly with limited initial information.
- **Dive Deep:** used logs, stage isolation, and reproduction to find the real
buffer-state cause.
- **Ownership:** treated it as a factory-throughput issue, not just a local
software bug.
- **Deliver Results:** restored production flow with a defensive prevention
mechanism.

#### Interview Emphasis

- Say what was uncertain at the start: device, PCB, or communication sequence.
- Explain the decision under time pressure.
- Emphasise robust prevention: known clean state at each new unlock start, not
only a symptom patch.

One-line recall:

Factory unlock failures → logs/stage isolation/reproduction → stale message
buffers + buffer-in-use flag → fix flag + reinitialise buffers at new-device
start → reliable production flow.

### Tell me about how you would debug an embedded issue that only appears intermittently on real hardware, not in simulation or unit tests. 

**Evidence → reproduce → instrument carefully → isolate → fix → verify → prevent recurrence**

For an intermittent embedded issue, I would first avoid jumping straight into the code. I would collect as much evidence as possible: 
logs, firmware version, hardware revision, test setup, input conditions, timing, videos if available, and whether the issue 
appeared after a recent software or hardware change.

Then I would try to reproduce it in a controlled setup. If it only happens rarely, I would add targeted instrumentation rather than 
broad logging, because too much logging can change timing. For example, I might stream key state variables or sensor samples over UART,
store a small circular debug buffer, or toggle a GPIO around suspicious sections so I can observe timing on a logic analyser or 
oscilloscope.

Once I had evidence, I would narrow the problem by subsystem: inputs and sensors, timing, interrupts, RTOS scheduling, shared data,
state-machine transitions, memory corruption, communication buses, and hardware signal integrity. If I suspected software, I would use
JTAG breakpoints or watchpoints where possible, but I would be careful because breakpoints can disturb real-time behaviour.

After identifying the root cause, I would make the smallest safe fix and then confirm it under the same conditions that reproduced the issue. 
I would also add a regression test orrhardware-in-the-loop test if possible, and document the evidence so the team can trust that the fix 
addresses the actual cause rather than just hiding the symptom.

## October 1 story selection and preparation status

Reuse the strongest 4–5 stories across several LPs. Every answer must withstand: **Situation -> problem -> my action -> why -> result -> lesson**. Separate observed facts, remembered implementation, and details to verify. Do not invent numbers or mechanisms.

- **STS factory failure:** Dive Deep, Ownership, Deliver Results, Highest Standards.
- **Touch-sense wrong first fix:** Learn and Be Curious, Dive Deep, Ownership, Highest Standards. Strongest failure/lesson story.
- **UIB:** Invent and Simplify, Ownership, Deliver Results.
- **SPI LED interrupts/loopback:** Dive Deep, Highest Standards, Ownership.
- **Recovery/reprogramming factory containment:** Bias for Action, Ownership, Deliver Results, Customer Obsession. Reuse [[#Story: Field-device recovery tool for corrupted configuration]] and the documented factory unlock story; retain each story's actual context.

Breadth is largely complete. Remaining value: concise execution, interview simulation, binary-search/stack boundary discipline, embedded spec translation/debugging, and probing the strongest LP stories. Kernel-driver/filesystem topics remain deprioritized.

### Story: STS factory calibration failure

- **Situation/problem:** approximately 5% factory calibration failures on the skin-tone sensor (STS). Initial hypothesis was comms/test-machine retries or buffering.
- **My action/why:** built test firmware, used diagnostic tooling on the factory floor, captured samples, and compared historical factory logs to isolate the cause and rule out comms/buffering.
- **Root cause:** LED did not turn on when expected during calibration. Indexing/integer underflow produced a negative value that became a huge `uint16_t`, corrupting the calibration average. Verify the exact arithmetic/types from code before describing the conversion more precisely.
- **Fix:** replaced simple accumulating averaging with sliding/settling-window logic; skipped zero/problem samples and continued until a settled reading. New sample had to be within the agreed range of the previous/old value (recalled roughly 3–4 points; exact reference/range to verify).
- **Validation/result:** reproduced the failure condition; forced a zero-buffer scenario in integration tests and checked that the function skipped zeros and continued until settle status. **Post-fix factory failure rate: [capture if known; not yet supplied].**
- **Lesson:** instrument and reproduce before accepting the initial comms explanation; make invalid samples and settling criteria explicit.
- **Probe:** Which arithmetic wrapped? Why was LED late? Why this window/range? How did evidence exclude comms? Which regression cases and production metric prove the result?

### Story: Touch-sense startup drift — first fix was wrong

- **Situation/problem:** startup threshold drift was missed; initial hypothesis was that periodic drift compensation ran too infrequently.
- **First action:** ran compensation on every sample for the first approximately 5 seconds. This first fix was wrong/incomplete.
- **Evidence/why change:** higher-rate streaming (approximately 10 ms) plus JTAG showed the threshold drop occurred at boot and could continue beyond that window.
- **Revised fix:** rolling/sliding buffer followed startup threshold drops until stable, using the same percentage/range concept as the drift algorithm to define stability.
- **Result:** revised approach addressed the observed behavior; **quantified outcome and exact stability parameters: [confirm if remembered].** Do not invent a reduction rate.
- **Lesson:** replace a fixed timing assumption with evidence-based stability detection; own the failed first hypothesis.
- **Probe:** What did the first fix miss? What changed your mind? How did streaming/JTAG affect timing? How did you validate stability and prevent endless settling?

### Story: UIB manufacturing tooling

- **Situation/problem:** manufacturing across Cyden IPL products involved different device protocols and operator complexity.
- **My action/why:** Universal Interface Board (UIB) provided a common middle layer, framing factory messages into the correct known device protocol and supporting unlocking/configuration.
- **Result:** simplified the operator process and manufacturing complexity across products. **Concrete impact metric: [capture if remembered; no number supplied].**
- **Lesson/probe:** common tooling can simplify repeatable workflows; explain protocol selection, validation, unsupported commands/products, and your personal contribution. Confirm a concrete lesson from experience before presenting one as a recollection.

### Story: SPI LED interrupt-driven transfer and loopback

- **Recalled architecture:** LED chain driven by SPI master; fixed/static TX buffer, busy gating, interrupt-driven TX, and loopback/feedback from the end of the chain for verification.
- **Main context:** prepares the LED frame, obtains buffer ownership, starts transfer; verifies result and handles completion/errors outside the ISR.
- **ISR:** services peripheral and advances transfer state. Recalled TX-ready interrupt sends from shared TX buffer and disables TX-ready interrupt when buffer is empty. Buffer-empty is not necessarily final-bit transfer-complete: verify hardware semantics.
- **RX/timer/counter:** feedback used RX/timer/counter logic to recognise expected returned data. Recalled edge/count/byte figures were inconsistent; verify them from code rather than asserting a frame length.
- **Overflow/error:** discuss SPI overflow condition and incomplete/bad loopback as distinct error cases. **Exact overflow flag, timeout mechanism/duration, and cleanup/error path: [verify from source].** Do not assert a particular timer or timeout implementation from uncertain memory.
- **Ownership helper:** a busy flag is safe only within strict ownership and synchronized check/set/clear transitions. It is not magic race protection. TX buffer stays unchanged while transfer owns it.
- **Result/lesson:** feedback provided a verification path; precise outcome/metric is not supplied. Explain main vs ISR responsibilities clearly and defend how incomplete transfers terminate.
- **Probe:** Which interrupt and registers? What happens to a new update while busy? Who clears busy? Does TX empty mean complete? How are RX overflow, mismatched feedback, and timeout distinguished?

### Technical follow-up: static communications buffer

- Derive fixed size from **protocol maximum payload + framing overhead**, not an arbitrary “100 because I like it”. Today's HEADER/CMD/LEN/CHECKSUM frame needs `MAX_PAYLOAD + 4` bytes; other protocols may differ.
- Known bounded size supports static allocation and predictable memory use. Ring buffer queued communications; explain message boundaries, usable capacity, full policy, and ownership.
- Reject/flag oversize before copying; never overflow. Reject/defer/queue new work according to the actual design, and do not overwrite a buffer while transmit owns it.
- See [[../Job_training/embedded_questions/coding_questions_asked_interview/packet_validation]] and [[../Job_training/embedded_questions/coding_questions_asked_interview/circular_buffer]].

### Technical follow-ups: RTOS and project evidence

- Dyson FreeRTOS OTA: use only the recalled sequence in [[../Job_training/embedded_questions/rtos#Recalled Dyson FreeRTOS OTA flow]]. Exact primitives/priorities remain to confirm; scheduler does not wait for another task to finish.
- nRF/Zephyr e-paper is work in progress: [[../Job_training/embedded_questions/rtos#nRF / Zephyr e-paper project status]]. Verify completion/BUSY handling from source before tightening the answer.

### Hardware/software debugging toolbox — experience cues

- **Logic analyser:** communications waveform/protocol/timing investigation.
- **Oscilloscope:** hardware noise/contact behavior, capacitor discharge, and ripple investigation.
- **Diagnostic tooling/logs:** factory capture, live samples, and historical evidence, particularly STS.
- Tie each tool to the observation and decision it enabled; do not claim an unremembered measurement or instrument setup.
