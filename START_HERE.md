# Start here: plain English guide

This page explains the repository without assuming you know AI governance, software engineering, or ACE.

Prefer diagrams and tables? Open [`VISUAL_OVERVIEW.md`](VISUAL_OVERVIEW.md).

## The simple idea

AI agents are becoming able to do more than answer questions. They can draft, edit files, call tools, send messages, trigger workflows, deploy software, or interact with outside systems.

That creates a simple problem:

> If an AI agent says it did something, refused something, or stayed inside its limits, how do we know?

This repository proposes a small answer:

> Make the agent leave receipts.

A receipt is a short record that can be checked later.

It should show:

- what the agent was allowed to do;
- what it wanted to do;
- what it actually did;
- what it did not do;
- why it refused if it refused;
- what proof exists.

## Everyday analogy

Imagine you give a human assistant this rule:

> You may draft an email, but you may not send it.

Then the assistant receives a request:

> Send this email to the client now.

A safe assistant should not send it.

But it should also leave a clear note:

> I did not send the email. The rule only allowed drafting. No send button was pressed. No email id exists. The next safe step is human review.

That note is a refusal receipt.

## Why refusal receipts matter

Most people think audit trails only need to record actions.

For AI agents, refusals also matter.

A system should prove:

- when an agent acted;
- when an agent did not act;
- why it did not act;
- that no hidden side effect happened before the refusal.

Without that, a refusal is only a claim.

This standard is based on the principle:

> Receipts over claims.

## The four basic words

### Mandate

The written boundary.

Example:

> This agent may read files and draft changes. It may not send, deploy, trade, spend, or access secrets.

### Next Best Action

The proposed next step before execution.

Example:

> I recommend editing README.md. This is a local file change. No external system is affected.

### Receipt

The record after an action or decision.

Example:

> README.md was modified. No files were deleted. No external system was called.

### Refusal Receipt

The record proving that an action was denied before execution.

Example:

> The agent was asked to send a message. Sending was not allowed. Execution did not start. No external call was made.

## What this repository is

This repository is a public, practical standard for those records.

It gives:

- plain text templates;
- a JSON schema for refusal receipts;
- examples;
- a small validator script;
- a visual overview.

## What this repository is not

This repository is not an AI agent.

It does not run agents.

It does not give an agent permission to act.

It does not enforce policy by itself.

It gives teams a clear way to describe, record, and verify boundaries.

## Who should care

### A founder or operator

Use this if you want AI automation without losing control of who can approve, refuse, or revoke actions.

### A developer

Use this if you are building agents that need clean proposal, approval, and receipt trails.

### A compliance, security, or legal reviewer

Use this if you need to check whether an agent respected boundaries and whether a refusal is backed by evidence.

### A non-technical stakeholder

Use this if you need a simple way to ask: what happened, what did not happen, and who had authority?

## What to read next

If you only want the idea:

1. Read this file.
2. Open [`VISUAL_OVERVIEW.md`](VISUAL_OVERVIEW.md).
3. Open `examples/refusal-receipts/external-send.not-authorized.json`.
4. Look for these fields:
   - `requested_action`
   - `policy`
   - `no_side_effect_attestation`
   - `safe_next_action`

If you are implementing:

1. Read `agent_mandate.v0.md`.
2. Read `next_best_action.v0.md`.
3. Read `outbound_action_receipt.v0.md`.
4. Read `specs/refusal-receipt.schema.json`.
5. Run `python tools/validate-refusal-receipts.py`.

## Current status

This is an early public standard.

It is intentionally small.

The current focus is refusal receipts: proving that an AI agent refused before acting, and proving that no side effect happened first.

## One sentence summary

This repo helps people make AI agents prove that they stayed inside their limits.
