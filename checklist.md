# Can this agent act, or only propose?

Use this checklist before allowing an AI agent to affect anything outside its own draft.

## 1. Mandate

- [ ] Is there a written mandate?
- [ ] Is the agent role explicit?
- [ ] Are allowed actions listed?
- [ ] Are forbidden actions listed?
- [ ] Is the stop condition clear?
- [ ] Is the human operator identified?

## 2. Action class

- [ ] Is this read-only?
- [ ] Is this draft-only?
- [ ] Does this mutate files?
- [ ] Does this affect external systems?
- [ ] Does this send a message, publish, deploy, trade, spend, sign, or transfer?
- [ ] Does this require human approval?

## 3. Evidence

- [ ] What source was read?
- [ ] What file or system would change?
- [ ] What receipt will be produced?
- [ ] Can the action be reversed?
- [ ] Is there a before/after diff?

## 4. Authority

- [ ] Is approval explicit?
- [ ] Is approval fresh?
- [ ] Is approval scoped?
- [ ] Is approval revocable?
- [ ] Is the agent confusing a suggestion with permission?

## 5. Safe outcome

If any answer is unclear:

```text
The agent may propose.
The agent may not act.
```

If the action is sensitive:

```text
Human approval required.
Receipt required.
Revocation path required.
```
