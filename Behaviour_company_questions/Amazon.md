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

