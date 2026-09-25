# Amazon Interview Prep

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
- What values were operators allowed to change, and why?
- How did the write/verify step work?
- What happened after three failed retries?
- How did you validate the tool before giving it to warehouses?

One-line recall:

Corrupted field configuration → volunteered to adapt handset → constrained
approved values → pass/fail UI + instructions → write/verify + three retries
then safe fail → local warehouse recovery.

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
