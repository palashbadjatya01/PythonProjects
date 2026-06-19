# CCA Foundations — Practice Exam 4 (60 Questions)

---

## Question 1
**Question:** How can you best ensure Claude never uses slang?

* A) Use the Message Batches API.
* **B) Define a Formal Persona and a negative constraint: Do not use slang.**
* C) Use Extended Thinking for every sentence.
* D) Set temperature to 0.0.

**Answer: B**
**Explanation:** Negative constraints combined with a well-defined persona provide strong reliable steering for tone and style. While adjusting temperature or using extended thinking can influence reasoning and variety they do not inherently filter out stylistic elements like slang.


---

## Question 2
**Question:** Where is the Claude Code CLI theme configured?

* **A) Claude Code currently does not support custom CLI themes.**
* B) In global .Xresources.
* C) In .claudetheme.json.
* D) Via claude config --theme.

**Answer: A**
**Explanation:** Claude Code is a headless-first tool designed for speed productivity and functionality within your existing terminal environment. It does not currently provide native configuration hooks JSON files or CLI flags for altering its visual theme.


---

## Question 3
**Question:** Which MCP method allows a client to see instruction templates?

* **A) prompts/list**
* B) prompts/show
* C) templates/get
* D) mcp/list-prompts

**Answer: A**
**Explanation:** Under the Model Context Protocol specification instruction templates are exposed as Prompts. To discover the list of available prompts and templates that a server supports the client calls the prompts/list method.


---

## Question 4
**Question:** An architect needs to build a Rolling Window context strategy. What is a major risk of this approach?

* A) The cost per turn will raise exponentially.
* B) The model will start to hallucinate more in the first 5 turns.
* **C) The agent may lose Critical Information or instructions provided at the very beginning of the session.**
* D) Prompt Caching becomes 100% ineffective.

**Answer: C**
**Explanation:** As a conversation progresses a rolling window strategy discards the oldest messages to maintain a strict context size constraint. This creates a critical architectural risk where essential goals user preferences or data points established at the beginning of the session are permanently erased.


---

## Question 5
**Question:** Which field in an API error determines if you should retry a request immediately?

* A) status_code: 400
* B) error.message
* **C) error.type**
* D) error.id

**Answer: C**
**Explanation:** Type values like overloaded_error programmatically inform the engineer that the issue is transient and appropriate for an immediate retry with an exponential backoff strategy. The error.id field is strictly for support tracking and a 400 status code indicates a malformed client-side request that should not be retried without modifications.


---

## Question 6
**Question:** What is the token limit for the Output of a single Claude Sonnet request?

* A) 4096 tokens.
* B) 200000 tokens.
* **C) 8192 tokens.**
* D) Unlimited.

**Answer: C**
**Explanation:** The maximum number of tokens Claude can generate in a single response is currently 8192. While 200k tokens represents the input context window limit physical output limits exist due to compute constraints. Architects must plan for truncation or implement context management strategies if expecting very long generations.


---

## Question 7
**Question:** How can Claude Code Auto-Fix linting errors whenever it saves a file?

* A) The --auto-lint flag.
* **B) A PostToolUse hook that runs eslint --fix.**
* C) An entry in CLAUDE.md.
* D) A cron job every 60 seconds.

**Answer: B**
**Explanation:** Post-tool hooks are the standard way to trigger side effects after an agentic action. Setting up automation via the hook system ensures the linter executes consistently after file modifications.


---

## Question 8
**Question:** Which agentic architecture is best for scanning 50000 documents for specific clauses?

* **A) Parallel Worker Pattern: A Coordinator distributes batches to 50 independent subagents.**
* B) Extended Thinking Mode
* C) Sequential Chain
* D) Single-Agent with 200k Context

**Answer: A**
**Explanation:** Parallelism is the most efficient and scalable way to handle high-volume independent data processing tasks. A sequential chain would be far too slow and a single agent context window can only hold a small fraction of 50000 documents at once.


---

## Question 9
**Question:** A engineer wants Claude Code to always follow a specific style for Git commit messages. Where should this be defined?

* **A) The CLAUDE.md file in the project root.**
* B) The package.json description field.
* C) The .claudeignore file.
* D) The user global .bashrc file.

**Answer: A**
**Explanation:** CLAUDE.md is the authoritative initialization and guide file that Claude Code checks in the project root for development conventions code style guides and command instructions.


---

## Question 10
**Question:** In RAG a model struggles to find an answer buried in 50 retrieved chunks. What is the likely issue?

* A) Prompt Caching is invalidating results.
* **B) The Lost in the Middle phenomenon.**
* C) The chunks are too small.
* D) The temperature is too low.

**Answer: B**
**Explanation:** Models often struggle to attend to information placed in the middle of a very long context window showing much better retrieval performance for data located at the very beginning or the very end. Implementing a reranking step to place the most relevant information in high-attention areas is essential.


---

## Question 11
**Question:** An MCP search-docs tool returns 50000 words. How to prevent context overflow?

* A) Instruct agent to only read 100 words.
* B) MCP server splits response into 50 results.
* **C) Tool should return a Summary and Deep-Link IDs for sections.**
* D) Use Prompt Caching for the 50000 words.

**Answer: C**
**Explanation:** Tools should be context-aware and avoid dumping massive amounts of raw data into the context window. Designing high-signal tools that summarize large datasets and provide target deep-link IDs allows the agent to efficiently scan the information and request specific sections only when needed.


---

## Question 12
**Question:** How to best prevent a medical report agent from including personal patient info PHI?

* **A) Use a Redaction Agent to strip PHI before the Findings agent.**
* B) Set temperature to 0.0.
* C) Tell the model Do not include PHI in the system prompt.
* D) Use Extended Thinking to identify PHI.

**Answer: A**
**Explanation:** Data privacy and compliance require defensive multi-stage architecture rather than relying entirely on a single prompt or setting. Introducing a dedicated preprocessing step such as a specialized Redaction Agent to strip sensitive information before passing data to downstream logic safeguards privacy programmatically.


---

## Question 13
**Question:** In medical diagnosis support which stop_reason is a critical error?

* A) stop_sequence
* B) tool_use
* C) end_turn
* **D) max_tokens**

**Answer: D**
**Explanation:** In diagnostics truncation means the model reasoning or output is incomplete creating a significant safety risk. Monitoring for unintended truncation via max_tokens is vital for safety-critical applications.


---

## Question 14
**Question:** What is the most critical safety feature for a Travel Booking agent that Pre-Books flights?

* A) Double-check the flight price using a second subagent.
* B) The subagent should have a 10000 token thinking budget.
* C) Use a larger model.
* **D) The pre-book tool should return a Draft ID and require user confirmation.**

**Answer: D**
**Explanation:** Financial and irreversible actions must always have a human-in-the-loop confirmation step to prevent accidental or unauthorized spending.


---

## Question 15
**Question:** What is the best way to prevent Claude Code from ever seeing your node_modules directory?

* **A) Add node_modules/ to the project .claudeignore file.**
* B) Mention Do not look in every prompt.
* C) Rename the folder to forbidden.
* D) Set the directory to Hidden in OS settings.

**Answer: A**
**Explanation:** The .claudeignore file is the primary and most robust way to sandbox the agent view of your local file system ensuring it ignores specified directories entirely.


---

## Question 16
**Question:** A PreToolUse hook in Claude Code is supposed to run tests but never triggers. Why?

* A) The engineer is using Extended Thinking.
* B) The engineer forgot to run claude hook-sync.
* C) The hook file does not have execution permissions.
* **D) Hooks are only triggered by matching tool calls.**

**Answer: D**
**Explanation:** Hooks in Claude Code are strictly event-driven. They do not run automatically on a generic timer or file save unless a matching tool execution event triggers them. The core architectural reason a hook entirely fails to fire is a mismatch in the defined tool triggers.


---

## Question 17
**Question:** Which MCP SDK class creates a client for multiple remote servers?

* A) ProtocolServer
* B) StdioClient
* C) TransportController
* **D) MultiServerClient or similar orchestrator class**

**Answer: D**
**Explanation:** The Model Context Protocol SDKs provide dedicated orchestrator or multi-client abstraction classes designed to aggregate connect and manage communications across multiple concurrent remote servers.


---

## Question 18
**Question:** What is the best technique to reduce Noisy output for a log-analysis agent?

* **A) Build a Filter Subagent to remove Info logs.**
* B) Use Extended Thinking for every line.
* C) Tell agent Be concise.
* D) Raise temperature to 1.0.

**Answer: A**
**Explanation:** Preprocessing data to remove low-signal noise improves the main agent focus. Context management often involves a tiered approach where simpler logic filters data before sending it to a high-overhead reasoning step.


---

## Question 19
**Question:** How to verify a Prompt Cache Hit occurred for a request?

* A) Stop-reason is cache-hit.
* B) Model says I retrieved this from cache.
* **C) Check usage object in API response for cache_read_input_tokens.**
* D) Response is a different color.

**Answer: C**
**Explanation:** The usage object in the Anthropic API response provides an exact breakdown of tokens billed including cache_read_input_tokens for a cache hit and cache_creation_input_tokens when a cache is written.


---

## Question 20
**Question:** To prevent an agent from deleting host files while executing Python what is the best security measure?

* A) Set the MCP server to Read-Only.
* B) Use Extended Thinking to vet the code.
* C) Add Do not delete files to the tool description.
* **D) Run the Python execution environment in a Sandboxed instance such as Docker.**

**Answer: D**
**Explanation:** Security for executable tools must be enforced at the infrastructure level to prevent environmental harm. A Read-Only transport configuration does not prevent a Python script from performing OS-level writes once executed. Only a sandboxed environment like Docker provides a deterministic security boundary.


---

## Question 21
**Question:** How to most robustly ensure Secret Keys are never sent to Claude Code?

* **A) Use a .claudeignore file to exclude .env files.**
* B) Rename secret files to .secret.
* C) Tell Claude in CLAUDE.md to Never read .env.
* D) Rely on API PII filters.

**Answer: A**
**Explanation:** The .claudeignore file serves as the primary security boundary for preventing local sensitive data leaks ensuring blocked files are completely invisible to the agent file-system tools.


---

## Question 22
**Question:** How does Claude Code handle .gitignore files?

* A) It requires manual copying to .claudeignore.
* B) It only respects .gitignore with a flag.
* **C) It respects .gitignore and automatically excludes those files.**
* D) It ignores .gitignore completely.

**Answer: C**
**Explanation:** Claude Code is designed to integrate seamlessly with standard developer workflows. By default it automatically reads and respects the rules defined in your project .gitignore file ensuring it does not scan modify or expose untracked files unless explicitly told to do so.


---

## Question 23
**Question:** In a Multi-Agent Research system why prune the conversation history for subagents?

* **A) To minimize Context Noise and prevent subagents from being confused.**
* B) To prevent Stealing of data.
* C) Because subagents have small context windows.
* D) Because the API bills Input Tokens twice.

**Answer: A**
**Explanation:** Good agentic design involves information hiding giving an agent only what it needs. Passing an entire unpruned conversation history introduces unnecessary context noise which can cause the subagent to lose focus or hallucinate based on irrelevant past turns.


---

## Question 24
**Question:** What is the role of a Scratchpad in an agentic workflow?

* A) Cache frequently used images.
* B) Store credit card info.
* **C) A text file or context block to draft thoughts and intermediate plans.**
* D) Backup system prompt.

**Answer: C**
**Explanation:** Scratchpads act as an external working memory for agents during multi-step tasks. By allowing the model to write out thoughts track execution progress and draft intermediate plans in a designated context block it improves accuracy and prevents the agent from losing track of long-term goals.


---

## Question 25
**Question:** How should an Orchestrator handle a subagent stuck in an infinite loop?

* A) Switch to a larger model.
* B) Raise max_tokens.
* **C) Build a Timeout and Turn Limit in the Orchestrator code.**
* D) Send a follow-up message: Please hurry.

**Answer: C**
**Explanation:** Programmatic guardrails in the orchestration layer are the only reliable way to handle runaway execution and infinite loops. Raising max_tokens merely allows the loop to run longer and costs more money while conversational nudges do not fix broken tool or agent states.


---

## Question 26
**Question:** Which Zod schema correctly defines a mandatory string parameter called filename?

* A) filename: z.mandatoryString()
* B) filename: z.string().required()
* C) filename: string
* **D) filename: z.string()**

**Answer: D**
**Explanation:** In Zod properties are mandatory by default unless explicitly followed by the .optional() modifier. The methods z.mandatoryString() and .required() are not valid Zod API methods. A raw string type hint is invalid syntax for a Zod validator.


---

## Question 27
**Question:** Which Claude Code command is used to see a list of all files modified in the current session?

* **A) claude status**
* B) claude list-changes
* C) claude diff
* D) claude log

**Answer: A**
**Explanation:** The claude status command provides a summary of the current session state including a clean list of all modified files. While claude diff shows the specific line-by-line changes within files it is not the primary command for listing the affected files.


---

## Question 28
**Question:** An MCP query-db tool is slow and the agent keeps retrying. What is the fix?

* **A) Build Request ID tracking on the server to ignore duplicate retries.**
* B) Tell agent Only wait 2 seconds.
* C) Switch database provider.
* D) Raise temperature.

**Answer: A**
**Explanation:** Architectural fixes for distributed agent networks involve making systems resilient to latency via idempotency. Building request tracking and unique identifiers allows the database or MCP server layer to catch and ignore duplicate retry attempts.


---

## Question 29
**Question:** Which Stop Sequence prevents a model from hallucinating examples if none are found in RAG context?

* A) Use temperature 0.0.
* **B) Use a custom sequence like END-OF-EXAMPLES and instruct the model to stop if no data exists.**
* C) Set max_tokens to 50.
* D) Use tool_use as a stop sequence.

**Answer: B**
**Explanation:** Stop sequences provide a programmatic kill switch for generation based on text markers making them an effective way to force the model to cease generation at a semantic boundary. Setting temperature to 0.0 only ensures determinism but does not prevent hallucinations.


---

## Question 30
**Question:** If a session has 4 matching cached prefixes which one will the model use?

* A) The First matching prefix.
* B) One at random.
* C) All 4 prefixes combined.
* **D) The Longest matching prefix that is currently in the cache.**

**Answer: D**
**Explanation:** Caching logic always prioritizes the largest valid anchor the longest matching prefix to maximize token savings. Caching is entirely deterministic meaning it does not involve randomness.


---

## Question 31
**Question:** A engineer is using Extended Thinking and the response is cut off. How can this be fixed?

* A) Set temperature to 0.0.
* **B) Raise the max_tokens parameter to be greater than the budget_tokens.**
* C) Enable Prompt Caching for thinking.
* D) Decrease the budget_tokens to 1000.

**Answer: B**
**Explanation:** The max_tokens limit must accommodate both the internal reasoning tokens and the final visible response tokens. If max_tokens is set too close to the thinking budget the model will run out of allocated tokens before finishing the actual answer leading to a truncated response.


---

## Question 32
**Question:** Where should API Keys for an MCP server legacy backend be stored?

* **A) In the environment variables of the MCP server process.**
* B) Hardcoded in tool-description.
* C) Passed as an argument from the client.
* D) In a public CLAUDE.md file.

**Answer: A**
**Explanation:** MCP servers act as proxies and should manage their own authentication internally rather than exposing sensitive credentials to the client or the AI model. Storing keys in the server environment variables keeps them secure.


---

## Question 33
**Question:** An MCP tool parameter can only be metric or imperial. How is this defined in Zod?

* A) units: z.union(['metric', 'imperial'])
* **B) units: z.enum(['metric', 'imperial'])**
* C) units: z.string().options(['metric', 'imperial'])
* D) units: z.string().regex(/metric|imperial/)

**Answer: B**
**Explanation:** The .enum() method in Zod restricts a parameter to a specific set of allowed string values which perfectly aligns with tool schema specifications. Options like .options() do not exist in Zod.


---

## Question 34
**Question:** Which role is required for the message containing tool_result blocks?

* A) tool
* B) system
* C) assistant
* **D) user**

**Answer: D**
**Explanation:** In the Anthropic Messages API when returning the results of a tool execution back to the model the message must be sent with the user role. The content array of this message contains the tool_result blocks matching the corresponding tool_use IDs from the previous assistant turn.


---

## Question 35
**Question:** Architecture for a News Summarizer checking 10 feeds every hour?

* **A) Scheduled Worker: simple agentic script on a timer.**
* B) Coordinator-Subagent.
* C) Multi-Agent Swarm.
* D) Manual Claude Code execution.

**Answer: A**
**Explanation:** Choose the simplest architecture that meets requirements to save on cost and complexity. For a straightforward retrieval and processing task with no inter-dependencies between the feeds a complex hierarchy or multi-agent swarm is over-engineered.


---

## Question 36
**Question:** What is the Maximum TTL for a cached prompt in the Anthropic API?

* A) 1 hour.
* **B) 5 minutes.**
* C) Indefinite.
* D) 24 hours.

**Answer: B**
**Explanation:** Anthropic Prompt Caching uses an ephemeral activity-based cache that has a Time-To-Live of 5 minutes. This means the cached context is automatically cleared after 5 minutes of inactivity for that specific prefix.


---

## Question 37
**Question:** Which MCP protocol message allows a client to execute a function on the server?

* A) tools/list
* **B) tools/call**
* C) jsonrpc/call
* D) tools/execute

**Answer: B**
**Explanation:** In the Model Context Protocol specification executing a tool is handled via the tools/call request method. The client sends this message with the name of the tool and the arguments required by its schema and the server returns the result.


---

## Question 38
**Question:** An architect is designing a Multi-Step Research agent. The agent often forgets the original user goal after several tool-intensive turns. What is the best structural fix?

* A) Switch to the Message Batches API.
* B) Set temperature to 0.0.
* **C) Build a Pinned Context block in the system prompt that is programmatically updated with the Original Goal.**
* D) Raise the max_tokens limit to 100000.

**Answer: C**
**Explanation:** Goal persistence is best achieved by maintaining a State Anchor in the system instructions. Pinning the core mission in the system prompt ensures the primary objective remains in active attention throughout multi-turn tool interactions.


---

## Question 39
**Question:** Which API parameter limits the internal reasoning process in Claude Sonnet?

* A) top_p
* B) max_tokens
* **C) budget_tokens inside the thinking object**
* D) stop_sequences

**Answer: C**
**Explanation:** The budget_tokens field sets a hard limit on the number of tokens used during the internal chain-of-thought extended thinking process. While max_tokens limits the size of the entire API response it cannot be used to isolate or control the reasoning phase alone.


---

## Question 40
**Question:** How to ensure ISO 8601 formatting when extracting dates?

* **A) Use format: date in JSON Schema and add a description.**
* B) Tell model Think in ISO format.
* C) Set temperature to 0.0.
* D) Use a few-shot example.

**Answer: A**
**Explanation:** Standardization in structured data extraction is most reliably achieved through constraint-led schema design. Combining standard schema types and built-in formats with explicit descriptions provides a hard syntactic boundary for the model output.


---

## Question 41
**Question:** In the Claude Agent SDK what is the purpose of an Agent Monitor?

* A) To rewrite the agent prompt.
* B) To act as a firewall.
* C) To restart the agent if it hits rate limits.
* **D) To track and log the agent turns tokens and tool calls for auditing.**

**Answer: D**
**Explanation:** Monitors provide crucial visibility and observability into the agentic loop allowing engineers to track audit and optimize performance and cost. They act as read-only observers rather than functional firewalls prompt rewriters or execution handlers.


---

## Question 42
**Question:** A Manager agent keeps assigning tasks to the wrong subagents. What is the fix?

* A) Switch Manager to a smaller model.
* **B) Improve the Descriptions of subagents in the Manager prompt.**
* C) Set Manager temperature to 1.0.
* D) Give Manager larger max_tokens.

**Answer: B**
**Explanation:** Agents rely on descriptions to understand the capabilities and boundaries of their tools. Effective delegation depends on clear high-signal metadata about agent capabilities.


---

## Question 43
**Question:** Which MCP transport is best for connecting a web-based IDE to a remote server?

* A) WebSockets.
* B) Stdio.
* C) GraphQL.
* **D) SSE Server-Sent Events**

**Answer: D**
**Explanation:** SSE is the standard transport protocol for MCP over HTTP making it ideal for web-based or remote connections. While Stdio is excellent for local process communication it cannot manage web-to-remote connections.


---

## Question 44
**Question:** Which pattern ensures a Coding Assistant does not break the build?

* A) Parallel Coding: pick the best looking.
* **B) Test-Driven Execution: write a test write code run Run-Test tool.**
* C) Extended Thinking to simulate build.
* D) Human-Review: every line approved.

**Answer: B**
**Explanation:** Closing the feedback loop with environmental tools is key to autonomous success. Reliability is best achieved by giving agents tools to self-verify against objective criteria. Models cannot perfectly simulate a complex local build through reasoning alone.


---

## Question 45
**Question:** When using the tool_choice parameter with type tool what happens if the model identifies that it needs to call a different tool first?

* **A) The model is forced to call the specified tool anyway even if it is logically incorrect.**
* B) The model will ignore the tool_choice and call the tool it thinks is best.
* C) The API will return a 400 Validation Error.
* D) The model will provide a long conversational explanation.

**Answer: A**
**Explanation:** Forced tool use overrides the model autonomy forcing it into a specific tool call regardless of its reasoning. The API strictly enforces the parameter meaning the model cannot deviate to call a prerequisite tool first or fall back to conversational text.


---

## Question 46
**Question:** **Question 1**

* A) Switch to a faster model.
* **B) Provide a Security Checklist tool that it must call and fill out.**
* C) Instruct the Coder to be secure.
* D) Raise temperature to 0.8.

**Answer: B**
**Explanation:** Gating a verdict behind a tool use ensures a systematic process rather than superficial assessment. Reliability is often a matter of process enforcement via tool-use constraints.


---

## Question 47
**Question:** A engineer wants to extract 100 names from a PDF. Which tool definition is most efficient?

* A) A tool that takes a single raw-text string.
* **B) A tool named submit-names that accepts an array of objects.**
* C) A tool named submit-name called 100 times.
* D) A tool that takes a CSV-string as input.

**Answer: B**
**Explanation:** Designing for high throughput and efficiency involves using collection types like arrays in tool schemas. Submitting multiple items wrapped in a single JSON array is significantly faster and uses far fewer tokens than making 100 individual sequential tool calls.


---

## Question 48
**Question:** A engineer wants Claude to output a list of users in a very specific XML format. Which technique is most effective?

* **A) Provide a Few-Shot example of the XML structure and a detailed schema definition.**
* B) Set the temperature to 1.0.
* C) Use Extended Thinking to plan tags.
* D) Tell the model to Be a professional XML engineer.

**Answer: A**
**Explanation:** Structural alignment is best achieved through exemplars and explicit constraints. Few-shotting is the most reliable way to align the model output to a non-JSON format whereas a high temperature increases randomness which is the opposite of what is needed for strict formatting.


---

## Question 49
**Question:** What is the most efficient way to Undo the last 3 changes Claude Code made?

* A) Delete the CLAUDE.md file.
* B) Restart with the --fresh flag.
* **C) Use git checkout or git revert via the terminal.**
* D) Tell Claude Please undo.

**Answer: C**
**Explanation:** Claude Code operates directly on your local Git repository making native version control commands the fastest and most reliable way to manage and revert state. Asking the agent to undo changes manually is slower and more prone to errors.


---

## Question 50
**Question:** How should a RAG system with 10k token Personal Profiles per user be cached?

* A) Add a cache breakpoint to every message.
* B) Cache only the System Prompt.
* C) Combine all profiles into a Global Cache.
* **D) Place the Personal Profile after the System Prompt with a breakpoint.**

**Answer: D**
**Explanation:** By structuring the prompt to place user-specific semi-static content like a 10k token Personal Profile right after the static system prompt and marking it with a cache breakpoint you create a highly reusable prefix for that user session. This reduces latency and API costs for subsequent turns.


---

## Question 51
**Question:** Which MCP feature allows a engineer to Group multiple related tools?

* A) Tool-Clusters.
* B) MCP-Packages.
* **C) The protocol does not have native Grouping. Use multiple servers.**
* D) Namespaces.

**Answer: C**
**Explanation:** MCP provides a flat list of tools. Grouping is handled by using different servers for domains. Architects should use multiple servers to create boundaries between tool sets.


---

## Question 52
**Question:** Which file defines Global Variables that the Claude Code agent should use across all files?

* **A) CLAUDE.md**
* B) .claude-globals.json
* C) The project README.md file.
* D) The .env file.

**Answer: A**
**Explanation:** CLAUDE.md is the central repository for project-wide context including standards build instructions and global variables preferred by the agent. While README files are geared toward human engineers and .env files handle environment configurations Claude Code specifically prioritizes reading instructions from CLAUDE.md.


---

## Question 53
**Question:** How does Prompt Caching impact the latency of a second-time request Cache Hit?

* A) The second request is slower.
* B) The first request is 10x faster.
* C) Both requests take the same time.
* **D) The second request is significantly faster.**

**Answer: D**
**Explanation:** Reading from the prompt cache is a high-speed operation. Cache hits reduce the Time-To-First-Token because the model does not have to re-process the cached prefix resulting in a significantly faster response time.


---

## Question 54
**Question:** How is Claude Code restricted to edit only files within the /src directory?

* A) Use a PreToolUse hook.
* B) Set ALLOWED_DIR in environment.
* C) Add /src to .claudeignore.
* **D) Run Claude Code from within the /src directory.**

**Answer: D**
**Explanation:** Claude Code determines its file access boundary based on its launch location. Launching the CLI from within a specific subdirectory naturally sandboxes the agent preventing it from reading or modifying parent or sibling directories outside of that path context.


---

## Question 55
**Question:** A Validator agent keeps marking correct code as Incorrect. What is the most likely cause?

* A) The temperature of the Validator is 0.0.
* **B) The Validator system prompt is too vague or overly restrictive.**
* C) The system is hitting API rate limits.
* D) The Coder agent is using a model that is too small.

**Answer: B**
**Explanation:** Vague prompts or overly rigid guidelines lead to high false-positive rates where correct functional code is flagged as incorrect due to a lack of precise rubrics. Setting temperature to 0.0 generally increases consistency rather than causing persistent misinterpretations.


---

## Question 56
**Question:** A JSON array of 500 items is malformed due to max_tokens limit. Best recovery?

* A) Raise temperature.
* B) Tell model to Be faster.
* C) Manually add closing tags.
* **D) Send truncated JSON back and ask model to Continue.**

**Answer: D**
**Explanation:** Using the Continue pattern allows the model to resume and complete structured data from exactly where it was cut off. Raising the temperature introduces randomness which actually makes the model less likely to produce valid long-form syntax.


---

## Question 57
**Question:** Extraction tool for Prices returns symbols like dollar sign instead of numbers. What is the fix?

* A) Tell the model Be a mathematician.
* B) Set top_k to 1.
* C) Use Extended Thinking to subtract symbols.
* **D) Update the tool schema to type: number and add a description.**

**Answer: D**
**Explanation:** Strict type definitions and clear descriptions within the tool JSON schema are the most effective and reliable way to enforce structural formatting. Personas like Be a mathematician are too broad and unreliable.


---

## Question 58
**Question:** Which MCP concept allows a client to discover a list of static or dynamic documents that a server can provide as context?

* A) Prompts
* B) Tools
* C) Transports
* **D) Resources**

**Answer: D**
**Explanation:** Resources are a core primitive in the Model Context Protocol that allow servers to expose read-only data files logs or database records to a client as background context. While Tools are designed for taking actions Resources act like an application-controlled file system or data discovery mechanism.


---

## Question 59
**Question:** Model misses Self-Referential links in few-shot extraction. What is the fix?

* **A) Add a few-shot example showing a self-referential relationship.**
* B) Tell model Be thorough.
* C) Switch to a larger model.
* D) Set temperature to 1.0.

**Answer: A**
**Explanation:** Few-shotting is highly effective when examples cover specific edge cases complex patterns and diverse structured relationships that the model might otherwise overlook.


---

## Question 60
**Question:** How to pin a specific library version so Claude Code uses the correct syntax?

* A) Delete all other versions on the computer.
* B) Use the --version-lock flag.
* **C) List the library version and doc link in CLAUDE.md.**
* D) Install with npm install --save-exact.

**Answer: C**
**Explanation:** Providing technical anchors and documentation references in your project CLAUDE.md file is the standard way to guide the agent behavior and prevent it from hallucinating outdated or incorrect API syntax.


---
