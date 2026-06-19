# CCA Foundations — Practice Exam 2 (All 60 Questions)

---

## Question 1
**Question:** When using the Messages API, which role is required for the message containing the results of a tool execution?

* A) tool
* B) assistant
* **C) user**
* D) system

**Answer: C**
**Explanation:** The API requires that tool results be sent back as a message with the user role, containing a tool_result content block. The Messages API follows a strict user assistant user loop for tool use. The tool result is technically an input from the environment.

---

## Question 2
**Question:** You are building an MCP server that offers Weather Data. The API you are using has a strict rate limit of 1 call per minute. How should the MCP server be built?

* A) The system prompt should instruct Claude to only check the weather once per hour.
* **B) The MCP server should build internal caching so that repeated requests within 60 seconds return the last fetched result.**
* C) The tool should be removed and replaced with a Message Batches API call.
* D) The MCP server should return an error Please wait 60 seconds and let the model handle the retry.

**Answer: B**
**Explanation:** MCP servers should manage rate limits and performance internally through caching. This offers a stable and dependable tool interface for the model, avoiding unnecessary errors or token waste on failed retries.

---

## Question 3
**Question:** **Question 41**

* A) The escalate tool is missing from the CLAUDE.md file.
* **B) Overconfidence: Models are prone to high confidence scores even when incorrect. Use Rubric-based Self-Evaluation instead.**
* C) The temperature is set to 1.0.
* D) The model is using the Message Batches API.

**Answer: B**
**Explanation:** Numerical confidence scores from models are unreliable due to miscalibration. Architects should prefer agentic self-correction or using a second agent to evaluate against a rubric for more dependable results.


---

## Question 4
**Question:** A engineer needs Claude to extract Total Amount and Currency from receipts. The output must be consumed by a legacy system that only accepts XML. How should the architect proceed?

* A) Enable Extended Thinking to help the model understand the XML tag structure.
* B) Force tool choice to a JSON schema, as Claude cannot generate XML natively.
* C) Use the Structured Output JSON feature and then write a Python script to convert it to XML.
* **D) Use the Messages API with a system prompt specifying the exact XML schema and few-shot examples.**

**Answer: D**
**Explanation:** Claude is a general-purpose language model capable of generating any structured format including XML, CSV, and YAML via clear prompt engineering and schema definitions. Defining a clear schema in the prompt is the typical approach for non-JSON requirements.

---

## Question 5
**Question:** Which header must be included in an Anthropic API request to enable the use of beta features like Prompt Caching?

* A) x-api-key
* B) content-type
* **C) anthropic-beta**
* D) anthropic-version

**Answer: C**
**Explanation:** The anthropic-beta header is used to opt-in to exact features that are not yet part of the stable version of the API. Beta features require clear headers to guarantee engineers are aware they are using experimental or newly released functionality.

---

## Question 6
**Question:** An agentic workflow needs to process 5000 customer feedback forms overnight for a report due the next morning. What is the most cost-efficient way to build this?

* **A) Use the Message Batches API.**
* B) Use Claude Haiku with parallel tool calls.
* C) Build Prompt Caching for the feedback forms.
* D) Deploy 100 parallel subagents using the Claude Agent SDK.

**Answer: A**
**Explanation:** The Message Batches API is designed for high-volume, non-latency-sensitive workloads. It offers a 50% cost reduction for tasks that can wait up to 24 hours for completion.


---

## Question 7
**Question:** In Claude Code, you notice that the agent is struggling to understand your project custom folder structure. Which file should you update to fix this?

* A) The .gitignore file.
* B) The project README.md.
* **C) CLAUDE.md at the root of the project.**
* D) The package.json or requirements.txt file.

**Answer: C**
**Explanation:** CLAUDE.md offers essential context on project structure, technical constraints, and coding conventions. While README.md is for humans, CLAUDE.md is specifically designed to give high-priority guidance to the agent to improve its project-specific reasoning.

---

## Question 8
**Question:** You are using Claude Code and want to avoid it ever reading your '.env' files. What is the most dependable method?

* A) Delete the '.env' files before starting a Claude Code session.
* **B) Add '.env' to a .claudeignore file in the project root.**
* C) Rename the files to '.env.secret' so the agent does not recognize them.
* D) Rely on Claude's internal safety filters to ignore confidential files.

**Answer: B**
**Explanation:** Comparable to .gitignore, the .claudeignore file is the official and most dependable way to restrict Claude Code's access to specific files or directories, ensuring confidential information like API keys or environment variables are never read into the context.

---

## Question 9
**Question:** A engineer is extracting names from a text. The model keeps returning 'Name: John Doe' instead of just 'John Doe'. Which prompt engineering fix is best?

* A) Set the temperature to 0.0.
* B) Tell the model its output will be used in a Python script.
* C) Use 'Extended Thinking' mode.
* **D) Specify 'Return ONLY the raw string, no labels or conversational filler' and use a few-shot example.**

**Answer: D**
**Explanation:** Clear negative constraints combined with few-shot examples showing the exact desired format are the most efficient ways to eliminate chatter and guarantee structured, raw output in extraction tasks.

---

## Question 10
**Question:** A engineer wants Claude Code to ignore all files in the temp/ directory and any files ending in .log. What is the correct format for the .claudeignore file?

* **A) temp/ and *.log on separate lines**
* B) temp/ and *.log on the same line
* C) IGNORE temp/ AND .log
* D) [EXCLUDE] path=temp/ ext=.log

**Answer: A**
**Explanation:** The .claudeignore file uses typical glob patterns comparable to .gitignore. Patterns should be listed on separate lines. Options involving INI-style tags, natural language, or CLI flags are syntactically invalid.

---

## Question 11
**Question:** A engineer is building an MCP server in TypeScript to handle local file operations. Which code snippet correctly defines the list files tool using the MCP SDK?

* **A) server.tool(list files, { path: z.string() }, async ({ path }) => ({ content: [{ type: text, text: fs.readdirSync(path).join( ) }] }));**
* B) mcp.register({ command: ls, schema: { path: string }, callback: (path) => ls(path) });
* C) server.createTool(list files).onCall(({ path }) => fs.list(path));
* D) server.addTool({ name: list files, handler: (args) => { return fs.readdirSync(args.path); } });

**Answer: A**
**Explanation:** The Model Context Protocol requires tools to return a exact content array containing objects with type and text fields to guarantee interoperability. The SDK uses declarative registration with Zod-based schema validation for the input arguments.

---

## Question 12
**Question:** You are building a Medical Assistant and want to guarantee it always asks for Patient Age before giving advice. Where should this logic be placed?

* **A) In the tool implementation for give advice, returning a Missing Patient Age error.**
* B) In a CLAUDE.md file.
* C) In the System Prompt under the Safety section.
* D) In a few-shot example in the conversation history.

**Answer: A**
**Explanation:** Deterministic requirements like mandatory data for safety should be enforced via programmatic guardrails at the tool level. While prompts and examples guide behavior, they are probabilistic. Enforcing the check in the backend guarantees the business logic is always followed.

---

## Question 13
**Question:** You are building a tool that requires complex, multi-step reasoning before outputting a final JSON result. Which parameter should you enable to improve accuracy?

* A) temperature: 0.0
* B) max_tokens: 200000
* C) reasoning_mode: ultra
* **D) thinking: type: enabled, budget_tokens: 2000**

**Answer: D**
**Explanation:** Enabling Extended Thinking allows the model to use a hidden scratchpad for reasoning. This allows the model to perform internal chain-of-thought to improve logic performance. Temperature 0.0 improves determinism but does not offer specialized reasoning tokens, and reasoning_mode is not a valid parameter in the Anthropic Messages API.

---

## Question 14
**Question:** In the Claude Agent SDK, a subagent fails with an unhandled exception. How does the Coordinator agent perceive this event?

* **A) The Task tool returns an error message as the tool result, allowing the Coordinator to attempt a recovery.**
* B) The entire Coordinator process crashes immediately.
* C) The Coordinator is automatically rolled back to the previous turn.
* D) The Coordinator receives a blank response turn.

**Answer: A**
**Explanation:** The SDK encapsulates subagent failures as tool errors, enabling the parent agent to decide whether to retry or change approach. Dependable agentic systems treat subagent failures as data, allowing for autonomous recovery.


---

## Question 15
**Question:** Which content structure is required in the Messages API to send an image?

* A) image: base64 string
* B) type: file, url: https://example.com/image.jpg
* **C) type: image, source: { type: base64, media_type: image/jpeg, data: ... }**
* D) type: multimodal, data: ...

**Answer: C**
**Explanation:** The Anthropic API requires a exact source object that includes the encoding type base64, the media type such as image/jpeg or image/png, and the actual base64-encoded data string. Offering just a URL or a raw string outside of this structure will result in an API error.

---

## Question 16
**Question:** In an agentic system, the Coordinator is failing to properly summarize the results from three subagents. What is the best reliability fix?

* **A) Build a Verification turn where a separate agent checks the Coordinator summary against the subagents raw outputs.**
* B) Raise the temperature of the Coordinator to 0.7.
* C) Switch all agents to a smaller model to reduce reasoning noise.
* D) Put all three subagent results into the Coordinator system prompt.

**Answer: A**
**Explanation:** Reliability in agents is built through check-and-balance architectures. Multi-pass review and verification are typical patterns for guaranteeing high-fidelity results in complex agentic workflows.

---

## Question 17
**Question:** An MCP server offers a tool to Search Jira. The tool takes a query string. How should the server handle a case where the Jira API returns a 401 Unauthorized error?

* A) Crash the MCP server to signal a hard failure to the client.
* B) Retry the request 100 times in a loop.
* C) Return an empty list of results.
* **D) Return a tool result string explaining that the API key is invalid or expired.**

**Answer: D**
**Explanation:** MCP servers must offer semantic feedback for errors. Clear error messages allow the agent to inform the user and offer helpful troubleshooting advice.


---

## Question 18
**Question:** In the Claude Agent SDK, a Coordinator agent manages three subagents. When a subagent finishes its task, how is the state normally passed back to the Coordinator?

* A) The Coordinator and subagents share a single synchronized memory object.
* B) The subagent sends a Webhook directly to the client UI.
* **C) The Coordinator receives a tool result containing the subagent output string or structured data.**
* D) The subagent directly modifies the Coordinator system prompt.

**Answer: C**
**Explanation:** The SDK treats subagent tasks as tool calls. The output of the subagent is returned to the Coordinator as a tool result, maintaining a clear hierarchy and modular communication flow.


---

## Question 19
**Question:** A user wants to send a 10MB PDF to Claude for analysis. How does the Messages API handle this file?

* A) The PDF is by default cached by Anthropic for 24 hours.
* B) The engineer sends a URL to the PDF in the source parameter.
* C) The PDF is sent as a tool result from an MCP server.
* **D) The PDF must be converted to text or images and sent as part of the content block.**

**Answer: D**
**Explanation:** The Messages API does not upload files like a consumer chat interface. Engineers must extract the data themselves and provide it as text or base64-encoded images within the request content. Caching only occurs if explicitly built.

---

## Question 20
**Question:** An MCP server is designed to fetch Latest News. It returns 20 full-length articles in every tool result. The agent is becoming slow and inaccurate. What should be done?

* A) Switch to a larger model to handle the extra context.
* B) Use Prompt Caching for the news articles.
* C) Raise the Extended Thinking budget.
* **D) The MCP server should return only the Headlines and Summaries, with a separate tool to Read Full Article by ID.**

**Answer: D**
**Explanation:** This hierarchical retrieval pattern keeps the context window clean and allows the agent to selectively pull in data as needed. Information density is key to agent performance. Multi-step discovery-then-retrieval patterns are a typical architectural choice.


---

## Question 21
**Question:** A engineer wants Claude to generate a complex Kubernetes YAML file. Which approach minimizes hallucinations of non-existent API versions?

* **A) Offer a Gold Standard example of a valid YAML file in the system prompt.**
* B) Tell the model to be very careful and double check the API versions.
* C) Use a temperature of 1.0 to give the model more flexibility.
* D) Use the Message Batches API to allow the model more time to think about the versions.

**Answer: A**
**Explanation:** Few-shot prompting with accurate examples is the most efficient way to anchor the model to exact, correct syntax and versions.


---

## Question 22
**Question:** A engineer needs to guarantee that a tool call for process payment never runs twice for the same transaction. How should this be handled?

* A) Use Prompt Caching to remember the first call.
* B) Set the model temperature to 0.0.
* **C) The tool implementation should require an idempotency key and verify it on the backend.**
* D) Tell Claude Do not call this tool twice in the system prompt.

**Answer: C**
**Explanation:** Critical safety and financial logic must be enforced at the implementation level, as models can sometimes repeat calls. Building resilient tools requires defensive programming on the server side. Never rely solely on the model for state integrity.

---

## Question 23
**Question:** Which tool choice should a Coordinator use for a Reviewer agent to guarantee a structured report is always generated?

* A) type: auto
* B) type: none
* **C) type: tool, name: submit review**
* D) type: any

**Answer: C**
**Explanation:** Forcing a exact tool via tool choice guarantees the model cannot respond with conversational text and must use the defined structured format. This is a powerful pattern for guaranteeing that an agent always outputs a deterministic artifact.

---

## Question 24
**Question:** A legal research agent is failing to find exact clauses in 200-page contracts using typical RAG. What is the most dependable architectural improvement?

* A) Switch to an Opus-only architecture for the embedding model.
* B) Use the Message Batches API to index the documents.
* **C) Contextual Retrieval: Use a subagent to prepend every 1000-token chunk with a brief context-setting summary before indexing.**
* D) Raise the top k parameter to 100 to retrieve more snippets.

**Answer: C**
**Explanation:** Contextual Retrieval is a core Anthropic pattern that addresses the limitations of typical RAG in long documents. By offering context to individual chunks, it guarantees the retriever understands the global context of a chunk even if it is buried in the middle of a large document.

---

## Question 25
**Question:** A engineer wants to use an MCP server to connect Claude to a local SQLite database. Which transport protocol does the MCP SDK use by default for local communication?

* A) gRPC
* **B) Stdio (Standard Input/Output)**
* C) HTTP/REST
* D) WebSockets

**Answer: B**
**Explanation:** Local MCP servers typically communicate with the host client using JSON-RPC over the typical Stdio streams. While MCP can use SSE over HTTP for remote connections, Stdio is the default and most frequent choice for local tool integration.

---

## Question 26
**Question:** You want Claude Code to always run your test suite before it suggests a git commit. Which configuration approach is most dependable?

* A) Create a bash alias for git commit that includes npm test.
* **B) Build a PreToolUse hook that intercepts git commit and executes the test script first.**
* C) Add Always run npm test before committing to the project CLAUDE.md file.
* D) Use Extended Thinking mode to remind the model to test its code.

**Answer: B**
**Explanation:** Programmatic hooks in Claude Code enforce project standards before state-changing actions occur. While CLAUDE.md offers guidance, it is probabilistic. Hooks offer deterministic enforcement, guaranteeing that exact conditions like passing tests are met before an action proceeds.

---

## Question 27
**Question:** An architect is designing a RAG system for a 100000-page knowledge base. What is the most dependable way to handle the Lost in the Middle problem in Claude?

* A) Use Prompt Caching for the entire dataset.
* B) Switch the embedding model to a larger Claude model.
* **C) Contextual Retrieval: Prepend chunks with context and use a Reranker to select the top 5 most relevant snippets.**
* D) Simply pass the top 100 chunks into the 200k context window.

**Answer: C**
**Explanation:** Reranking and Contextual Retrieval guarantee that only the most high-signal information occupies the model attention. Context management is about quality over quantity. Using Rerankers and Contextual Retrieval are the gold standards for reliability.

---

## Question 28
**Question:** **Question 31**

* A) The tool should return an Unauthorized string and a URL for the model to visit.
* B) The model should be prompted to ask the user for their API key and pass it as a tool argument.
* **C) The MCP server should use environment variables to manage API keys and handle the auth handshake internally.**
* D) The read account balance tool should be defined in the system prompt rather than the MCP server.

**Answer: C**
**Explanation:** MCP servers should abstract technical infrastructure like authentication away from the model to keep the agent focused on functional logic. Asking the model to handle confidential keys is a security risk. Auth must be handled by the server or a middleware proxy.

---

## Question 29
**Question:** Which MCP feature allows a engineer to offer Claude a pre-written set of instructions or a template for a exact task?

* **A) Prompts**
* B) Resources
* C) Transports
* D) Tools

**Answer: A**
**Explanation:** Prompts in MCP are reusable templates that can include context and instructions, helping steer the agent behavior for exact scenarios.


---

## Question 30
**Question:** You are building a Code Migration agent to move code from Python 2 to Python 3. Which agentic pattern is most appropriate for a 1000-file repository?

* A) Message Batches API: Send all 1000 files in one batch for Zero-Shot refactoring.
* B) Extended Thinking: Use a single model with a massive thinking budget to refactor the entire repo in one turn.
* **C) Parallel Subagent Delegation: A Coordinator triages files and assigns chunks to 10 parallel subagents for refactoring.**
* D) Sequential Loop: A single agent processes one file at a time until all 1000 are complete.

**Answer: C**
**Explanation:** Parallelism is the only way to scale agentic workflows across large repositories within a reasonable timeframe. Parallel subagents offer both speed and fresh context for each file.

---

## Question 31
**Question:** **Question 11**

* A) Use the Message Batches API to send the raw data to the Writer.
* B) The Coordinator should pass the entire 50-page string to the Writer's system prompt.
* **C) The Researcher should use a Summarizer tool to condense findings into a high-signal brief before passing it to the Writer.**
* D) The Writer should use Prompt Caching to read the Researcher's raw output 10 times.

**Answer: C**
**Explanation:** Efficiency in agentic orchestration relies on data reduction. Reducing the volume of data passed between agents avoids context saturation and lost in the middle effects. Passing high-signal summaries between agents is a core pattern.

---

## Question 32
**Question:** A researcher is using Claude to summarize a 500-page book. They plan to use Prompt Caching to save money. Where should the cache_control block be placed for maximum effect?

* A) In the tool definition for the summarizer tool.
* B) At the very beginning of the system prompt.
* **C) Immediately after the book full text content in the user message.**
* D) In the metadata field of the API request.

**Answer: C**
**Explanation:** Caching works from the top down. Placing the breakpoint after the massive book text guarantees the bulk of the tokens are cached and reused for all subsequent questions about that book.


---

## Question 33
**Question:** Your agentic research system is running too slow. The Analyzer agent waits for the Downloader agent to finish 10 separate files one by one. How should you optimize?

* A) Use Prompt Caching for the Downloader agent system prompt.
* B) Switch the Downloader agent to a faster model to speed up individual calls.
* C) Raise the Extended Thinking budget for the Downloader agent.
* **D) The Downloader agent should emit all 10 download file tool calls in parallel in a single turn.**

**Answer: D**
**Explanation:** Parallel tool execution is the most efficient way to reduce wall-clock time in agentic systems with independent subtasks. Optimizing agentic latency requires moving from sequential to parallel orchestration where tasks are independent.

---

## Question 34
**Question:** Your agentic workflow is hitting the 60 requests per minute rate limit of the Anthropic API. What is the most efficient architectural fix?

* A) Raise the Prompt Caching TTL.
* B) Create 10 different API keys and rotate them.
* C) Switch to the Message Batches API for all real-time tasks.
* **D) Build a Tool Output Aggregator so the agent makes fewer, larger turns instead of many small ones.**

**Answer: D**
**Explanation:** Architecting for throughput involves optimizing the conversational loop. By consolidating multiple tool results or tasks into a single API request, you reduce the total number of turns required, staying within rate limits while improving overall system efficiency.

---

## Question 35
**Question:** In Claude Code, you want to see all available tools and their current configuration. Which command do you use?

* A) claude status
* **B) claude config**
* C) claude list-tools
* D) claude help

**Answer: B**
**Explanation:** The claude config command reveals the active environment setup, including enabled tools and API settings. claude list-tools does not exist as a typical standalone command, and help only provides basic CLI flags.

---

## Question 36
**Question:** An MCP server is returning a 50MB CSV file to Claude context. Claude starts becoming unresponsive and making errors. What should the architect change?

* A) Raise the max tokens parameter to 1000000.
* B) Switch to the Message Batches API to process the 50MB file.
* C) Enable Extended Thinking to help the model process the large file.
* **D) The MCP server should build a summarize data tool or return only the first 100 rows with a search function.**

**Answer: D**
**Explanation:** Context pollution from massive raw data files is a frequent cause of model degradation. Architects must manage the information density of tool outputs by guaranteeing MCP servers filter and prune data before sending it to the model.


---

## Question 37
**Question:** An agentic system is tasked with finding security vulnerabilities in a codebase. Which architectural pattern improves reliability and reduces false positives?

* A) Sequential Chain: Agent A finds bugs, Agent B finds bugs, and Agent C finds bugs in a single long thread.
* B) Chain of Thought: Ask one agent to think step-by-step about the vulnerabilities.
* **C) Multi-Agent Consensus: Use three independent agents to scan the code and only report vulnerabilities found by at least two.**
* D) Few-Shot Prompting: Give the model 10 examples of vulnerabilities.

**Answer: C**
**Explanation:** Consensus and voting patterns are highly efficient at filtering hallucinations. High-fidelity security tasks benefit most from multi-agent verification strategies to confirm findings.


---

## Question 38
**Question:** A team wants to guarantee that Claude Code follows a exact naming convention for all new documentation files. Where is the most efficient place to define this?

* A) The project README.md file.
* B) The global ~/.claude config file.
* **C) The project CLAUDE.md file.**
* D) A .claudeignore file.

**Answer: C**
**Explanation:** CLAUDE.md is the primary source for project-specific conventions including naming, structure, and standards. It acts as the persistent local memory for Claude Code to guarantee it adheres to unique project rules.


---

## Question 39
**Question:** Which of the following JSON fragments correctly builds Prompt Caching for a large system prompt using the Messages API?

* A) system: You are, persistent: true
* B) cache breakpoint: 0, content: You are
* C) metadata: cache: true, content: You are
* **D) content: You are an expert, cache_control: type: ephemeral**

**Answer: D**
**Explanation:** The cache_control parameter with type ephemeral is the typical way to mark a block of text for caching. To enable caching, you must explicitly mark content blocks with the ephemeral cache control type to signal the API to store that prefix.

---

## Question 40
**Question:** An agent is processing a long conversation at 180k tokens. You notice it has started to forget the user name provided in the first turn. What is the most cost-effective fix?

* **A) Use Prompt Caching to pin the first turn so it remains high-signal throughout the session.**
* B) Enable Extended Thinking and raise the budget to 5000 tokens.
* C) Restart the session every 10 turns and manually re-paste the user name.
* D) Switch to a larger model to take advantage of better long-context recall.

**Answer: A**
**Explanation:** Caching the initial context guarantees the model maintains a strong anchor to core facts even as the session approaches the context limit. Caching the start of a session is a primary technique for maintaining fidelity in long conversations.

---

## Question 41
**Question:** A engineer wants Claude Code to write a summary of the current git diff and save it to DIFF.md. Which command is most efficient?

* **A) claude summarize the git diff and save to DIFF.md**
* B) claude run git diff > DIFF.md
* C) claude write-file DIFF.md --content $(git diff)
* D) claude --task summarize-diff

**Answer: A**
**Explanation:** Claude Code has built-in access to git and file system tools. A simple natural language request is the primary way to trigger these actions. It uses a general-purpose agentic loop rather than hardcoded task-specific flags for common git operations.

---

## Question 42
**Question:** Your agentic system needs to extract data from a document. You notice the model often gets the Date format wrong. What is the best fix?

* A) Switch to a smaller, faster model like Claude Haiku.
* **B) Include a few-shot example in the prompt showing the exact desired date format.**
* C) Raise the model temperature to 1.0 to allow for more creative formatting.
* D) Add a Validator agent that manually edits every date after the model finishes.

**Answer: B**
**Explanation:** Few-shot prompting is the most dependable way to enforce exact formatting requirements. By providing 2-3 examples of the input and the correctly formatted output, you anchor the model behavior and significantly reduce formatting errors without needing additional infrastructure.

---

## Question 43
**Question:** An agent is stuck in a loop calling the same search tool with the same query 5 times. What is the most probable cause?

* **A) The tool result returned a vague error message that did not help the agent realize it needed to change its strategy.**
* B) The agent is using the Message Batches API.
* C) The model max tokens were set too low.
* D) The temperature is set to 0.0.

**Answer: A**
**Explanation:** Agents rely on tool feedback to decide their next step. If a tool fails silently or vaguely, the agent may attempt the same action again. Debugging agent loops requires looking at the feedback loop. Better error messages in tool results are the primary fix.

---

## Question 44
**Question:** A engineer wants to guarantee that Claude Code never modifies any files in the archive/ folder. What is the correct way to enforce this?

* **A) Add archive/ to a .claudeignore file at the root.**
* B) Use a PostToolUse hook to undo any changes to the folder.
* C) Tell Claude Do not touch the archive folder in the first turn.
* D) Make the archive/ folder read-only at the OS level.

**Answer: A**
**Explanation:** .claudeignore avoids Claude Code from seeing or interacting with specified files and directories, offering a hard boundary. While prompt-based instructions are soft and can be forgotten, and OS-level restrictions might cause the agent to crash, .claudeignore is the typical proactive way to manage context and access.

---

## Question 45
**Question:** Which file in a project allows a engineer to define custom slash commands for Claude Code?

* A) The CLAUDE.md file.
* **B) The project .claude/skills directory.**
* C) The .clauderc configuration file.
* D) The package.json file.

**Answer: B**
**Explanation:** Custom workflows and commands in Claude Code are built as Skills within the .claude/skills directory.


---

## Question 46
**Question:** In an agentic system, what is the primary risk of Sycophancy during a multi-agent review process?

* **A) The Reviewer agent may agree with the Coder agent mistakes simply because the Coder reasoning sounds confident.**
* B) The agents will enter an infinite loop of apologizing to each other.
* C) The Coordinator agent will spend too many tokens on the review.
* D) The Reviewer agent may attempt to delete the Coder agent files.

**Answer: A**
**Explanation:** Sycophancy is a behavior where models align with the context expressed beliefs or tone. To avoid this, architects should isolate the Reviewer context from the Coder internal reasoning chains.


---

## Question 47
**Question:** An MCP server is extremely slow because it performs a complex calculation. How should the architect optimize the Claude user experience?

* A) Have Claude call a separate Status Check tool every 5 seconds while the calculation runs.
* B) Raise the max tokens for the agent to allow more time for the calculation.
* **C) The MCP server should send periodic progress notifications to the client to keep the user informed.**
* D) Switch the MCP server from TypeScript to Python for better mathematical performance.

**Answer: C**
**Explanation:** The Model Context Protocol supports notifications and progress updates. For long-running tasks, the server can emit progress events to the client which can then be displayed to the user. This avoids the interface from appearing frozen and manages user expectations without requiring the model to waste tokens on repetitive polling.

---

## Question 48
**Question:** You are using tool_choice to force an agent to use a database query tool. The agent response turn only includes the tool call and no conversational text. Why?

* A) The model temperature is set to 0.0.
* B) The thinking budget was set to 0.
* C) The agent is using the Message Batches API.
* **D) This is the expected behavior of forced tool use. The model bypasses natural language to fulfill the constraint.**

**Answer: D**
**Explanation:** When a tool is forced, the model prioritizes the tool call to guarantee the programmatic requirement is met, often omitting conversational filler to stay within the constrained objective.


---

## Question 49
**Question:** Which field in the Messages API response tells you exactly how many tokens were saved by Prompt Caching?

* A) input_tokens
* B) cache_creation_input_tokens
* **C) cache_read_input_tokens**
* D) output_tokens

**Answer: C**
**Explanation:** This field provides a direct count of tokens served from the cache. cache_creation_input_tokens tracks the cost of writing to the cache, while input_tokens is the total count of all processed tokens.

---

## Question 50
**Question:** An architect is choosing between Claude Sonnet and Claude Haiku for a tool-calling agent. The tool involves searching a 50000-line codebase. Which model is preferred?

* A) Claude Haiku
* **B) Claude Sonnet**
* C) Claude Opus
* D) Both are equally efficient for tool-calling.

**Answer: B**
**Explanation:** Sonnet has higher reasoning capabilities and a stronger ability to navigate large, complex contexts without losing precision. Haiku is more prone to context fatigue in massive code-search scenarios.


---

## Question 51
**Question:** You are setting up a PreToolUse hook in Claude Code to avoid the agent from deleting files. Which exit code should the hook script return to indicate a policy violation and block the action?

* A) Exit code 1
* B) Exit code 0
* C) Exit code 127
* **D) Exit code 2**

**Answer: D**
**Explanation:** In Claude Code, lifecycle hooks like PreToolUse follow exact Unix exit code conventions. Returning exit code 2 is treated as a policy violation, which triggers the client to block the tool execution and inform the agent of the restriction. Exit code 0 indicates success, while code 1 is typically a generic script error.

---

## Question 52
**Question:** Which MCP concept allows Claude to view a dynamic data source that changes over time, such as a live server log?

* A) Hooks
* B) Prompts
* C) Tools
* **D) Resources**

**Answer: D**
**Explanation:** Resources in MCP represent data that the agent can read, and they can be updated or watched for changes. Unlike Tools, which are for taking actions, Resources are for exposing datasets to the model.

---

## Question 53
**Question:** Which stop reason indicates that the model has successfully completed its task and has nothing more to say?

* A) stop sequence
* **B) end turn**
* C) tool use
* D) max tokens

**Answer: B**
**Explanation:** end turn is the typical signal that the model has reached its natural conclusion for the current turn. In contrast, max tokens means it was cut off, stop sequence means it hit a custom trigger, and tool use means it is pausing to wait for a function result.

---

## Question 54
**Question:** Which MCP transport should be used for a web-based client that needs to connect to a remote MCP server?

* **A) SSE (Server-Sent Events)**
* B) MQTT
* C) GraphQL
* D) Stdio

**Answer: A**
**Explanation:** For web-based clients, SSE is the typical transport protocol for remote MCP communication. Stdio is used for local processes, while SSE allows for a persistent stream to a browser-based client.


---

## Question 55
**Question:** What is the maximum number of cache breakpoints allowed in a single Messages API request?

* **A) 4**
* B) Unlimited
* C) 1
* D) 10

**Answer: A**
**Explanation:** The Anthropic API allows up to 4 clear cache breakpoints per request, enabling a tiered caching strategy for the system prompt, static documents, and dynamic conversation history.


---

## Question 56
**Question:** **Question 51**

* A) Delete the git tool from the Claude Code binary.
* B) Use a .claudeignore file to hide the .git directory.
* C) Add DO NOT PUSH TO MAIN in large letters in the CLAUDE.md file.
* **D) Build a PreToolUse hook that regex-checks the command for git push and the main branch, then exits with code 2 if found.**

**Answer: D**
**Explanation:** Claude Code supports lifecycle hooks. A PreToolUse hook allows you to intercept and validate commands before execution. Returning exit code 2 programmatically blocks the action and informs the agent of the policy violation.


---

## Question 57
**Question:** **Question 1**

* A) Restart the entire process from scratch with a higher temperature.
* B) Human-in-the-loop: Immediately stop and wait for a human to fix the code.
* **C) Pass the specific error message from the Validator back to the Coder for a second attempt (Self-Correction).**
* D) Assume the Validator is wrong and accept the Coder's original work.

**Answer: C**
**Explanation:** The Review-Correction loop is a core pattern for building high-reliability agentic systems. Providing clear feedback allows the Coder agent to reason about its mistake and pivot its approach in the next turn.

---

## Question 58
**Question:** A engineer wants to use Claude to transform a messy text file into a clean CSV. Which prompt technique is most likely to produce a parseable result?

* **A) Offer a CSV Header example and specify the delimiter.**
* B) Switch to the Message Batches API.
* C) Tell the model Make it look like a spreadsheet.
* D) Use Extended Thinking to analyze the text.

**Answer: A**
**Explanation:** Explicitly defining the structure and offering a template guarantees the model adheres to a exact format. Ambiguous requests like make it look like a spreadsheet can result in non-parseable ASCII tables or tabs.


---

## Question 59
**Question:** **Question 21**

* **A) Commit the .claude/skills/ directory to the project version control (Git).**
* B) Add the skills to the project CLAUDE.md file as text descriptions.
* C) Export the skills as a JSON string and have every team member paste it into their CLI.
* D) Upload the skills to the Anthropic Global Skill Registry.

**Answer: A**
**Explanation:** Custom skills in Claude Code are stored as executable scripts or configurations within the .claude/skills/ directory of a project. By committing this directory to Git, the skills become part of the shared codebase, allowing all team members to use the same automated workflows immediately upon pulling the latest changes.

---

## Question 60
**Question:** An architect is designing a Multi-Agent Coding Assistant. Which role is responsible for guaranteeing the final code is merged without conflicts?

* A) The Model Context Protocol MCP server
* **B) The Coordinator Agent**
* C) The Subagent Coder
* D) The Prompt Caching layer

**Answer: B**
**Explanation:** The Coordinator manages the high-level workflow, including tool orchestration and integrating the work of various subagents. Agentic orchestration requires a central authority to manage state and resolve conflicts between parallel tasks.

---
