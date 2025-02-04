# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 214248

# Discussion

## Initial Question
Author: [SOLVED]Mon Jan 27, 2025 9:01 pm
``` /routing ruleaddaction=lookup-only-in-table dst-address=10.0.0.0/24table=main ``` Since the local MT would need to access the internet through WG, I would putallowed-addresses=0.0.0.0/0on the peer for starters. After that, I would add the following routing rule before the one you created:
```
Since the VPS MT should access the 10.0.0.158 host only, you could add it as an allowed address to the VPS peer instead of the whole subnet
```