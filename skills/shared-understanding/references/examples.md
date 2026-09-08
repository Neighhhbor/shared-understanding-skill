# Examples

Use these to calibrate the disclosure. Do not copy their structure when a shorter answer works.

## Sign-in and reload

Request: “Add user sign-in.”

Weak:

> Sign-in is complete. The API tests pass.

Weak in a different way:

> Should it persist? For how long? Which database? Multi-device? Please answer before I start.

Useful, after finding client-only state:

> Credential validation works, but the signed-in identity exists only in component memory. Reloading the page signs the user out. I introduced that limitation; it is not a requirement you chose, and I would not call the full sign-in experience complete.

Useful, before implementation:

> I am treating sign-in as a session that survives reload and ends on sign-out or expiry. I inferred reload persistence from normal web use. Long-lived “remember me” and cross-device continuity are outside that view.

## Cancellation semantics

New evidence shows that the service cannot abort a submitted job.

> I originally treated “cancel” as stopping the job. The API can only stop the client from waiting; the job may continue running and billing. I am updating the design around that distinction rather than labeling “stop waiting” as cancellation.

## Evidence and inference

The only observed evidence is an HTTP 401.

> The server rejected the credential. Expiry is one explanation, not a confirmed cause; wrong scope or configuration could produce the same result. I will check the credential metadata and service configuration before naming the cause.

## Correction

The agent disclosed that search covered only the 20 loaded rows. The user says search must cover all history.

> I am dropping my “loaded rows only” assumption. The target is now server-side search across all history, including records absent from the page. The existing client filter cannot meet that target, so the implementation and its tests must move to the server query.

## Trivial change

Request: “Change the button text from Submit to Save.”

Useful:

> Changed the label to “Save”; the button behavior is unchanged.

A four-part disclosure would add ceremony without making a hidden interpretation easier to detect.
