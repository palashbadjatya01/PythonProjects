# CCA Foundations — Practice Exam 5 (60 Questions)

---

## Question 1
**Question:** When using the Extended Thinking feature which stop_reason indicates that the model finished its reasoning but was cut off before finishing the final answer?

* A) thinking_complete
* **B) max_tokens**
* C) stop_sequence
* D) end_turn

**Answer: B**
**Explanation:** If the total token allocation which includes both the extended thinking tokens and the visible output tokens is exhausted before the model completely finishes generating its final response the stop_reason returned will be max_tokens. A stop_reason of end_turn means the model finished the entire message successfully and thinking_complete is not a standard top-level API stop_reason.


---

## Question 2
**Question:** A engineer is using Claude Code to refactor a large legacy repository. They notice that Claude occasionally makes changes that violate the project specific architectural patterns. Which configuration would most effectively prevent these violations?

* A) Create a custom slash command for every refactoring task to include the rules.
* B) Use plan mode for every interaction to manually review the architectural approach.
* C) Update the global Claude Code system prompt via the CLI settings.
* **D) Add architectural guidelines to a CLAUDE.md file in the root directory.**

**Answer: D**
**Explanation:** CLAUDE.md is the standard and most effective mechanism for providing project-specific context development constraints and architectural guidelines that Claude Code proactively reads and follows during a session. While plan mode allows you to manually catch violations before they are written it is a reactive human-in-the-loop step rather than a configuration-based prevention rule.


---

## Question 3
**Question:** What is the primary difference between the ephemeral cache type and a persistent cache in modern LLM architectures like Anthropic Prompt Caching?

* A) Ephemeral cache only works for images while persistent works for text.
* B) Persistent cache is stored on the user local machine while ephemeral is in the cloud.
* C) Ephemeral cache is free while persistent cache costs 10x more.
* **D) Anthropic currently only supports an ephemeral cache which has a short Time-To-Live and is designed for session-based reuse.**

**Answer: D**
**Explanation:** Anthropic Prompt Caching implementation utilizes an ephemeral lifecycle model. Cache entries have a brief Time-To-Live typically expiring after 5 minutes of inactivity and are optimized for rapid session-based iteration such as multi-turn chat dialogues or continuous agent loops.


---

## Question 4
**Question:** A engineer is using Claude Code and wants to see a list of all currently active MCP servers and their available tools. Which command should they use?

* **A) claude mcp list in the terminal**
* B) mcp list
* C) claudecode --list-mcp
* D) Checking the CLAUDE.md file.

**Answer: A**
**Explanation:** The claude mcp list CLI command is the official way to display all configured active Model Context Protocol servers along with their available tools directly from your terminal. While a CLAUDE.md file is useful for providing static engineering instructions it does not reflect the dynamic runtime state of active process connections.


---

## Question 5
**Question:** An agent is using a tool to search a vector database. The database returns 50 chunks of text. What is the BEST way to provide this context to the LLM to avoid Attention Dilution?

* **A) Have a Ranker subagent or a scoring algorithm select the top 5-10 most relevant chunks before sending them to the final LLM.**
* B) Send all 50 chunks in a single large user message.
* C) Use the Batch API to process each chunk individually.
* D) Place all 50 chunks in a cache and tell the model where to find them.

**Answer: A**
**Explanation:** Providing too much irrelevant or noisy context to an LLM leads to attention dilution and can trigger the Lost in the Middle effect. Filtering scoring or reranking the retrieval results to pass only the top 5-10 most relevant chunks guarantees that the model stays focused on the most critical context.


---

## Question 6
**Question:** A engineer wants to track the Token Efficiency of their prompt caching implementation. Which calculation provides the Cache Hit Rate?

* **A) cache_read_input_tokens divided by input_tokens**
* B) cache_read_input_tokens minus cache_creation_input_tokens
* C) cache_creation_input_tokens divided by input_tokens
* D) output_tokens divided by input_tokens

**Answer: A**
**Explanation:** The cache hit rate is the ratio of tokens successfully served from the cache compared to the total input tokens processed in the request. Option 2 measures the cache write rate and option 4 represents net token savings rather than a rate or percentage.


---

## Question 7
**Question:** A coordinator agent is failing to correctly synthesize information from two subagents because the outputs from the subagents are too long causing the coordinator to hit its context limit. What is the best fix?

* A) Have the coordinator read the subagents outputs from a shared text file instead of receiving them in the message history.
* B) Switch the coordinator to a model with a smaller context window to force it to be faster.
* C) Tell the coordinator to ignore any output longer than 1000 tokens.
* **D) Instruct the subagents to provide their findings in a structured concise JSON format or bulleted summary.**

**Answer: D**
**Explanation:** Context management in multi-agent systems requires designing subagents to be high-signal low-noise in their reports. Constraining subagent output ensures that only the necessary information is passed back to the coordinator preserving valuable context space.


---

## Question 8
**Question:** You are building a research agent that uses a Web Search tool. The agent is getting hallucinated search results where it makes up URLs that do not exist. What is the best fix?

* A) Tell the agent You are a very honest researcher in the system prompt.
* **B) Require the agent to always output the raw text of the search result before summarizing it.**
* C) Raise the reasoning budget to 50000 tokens.
* D) Use a smaller model to save money on the hallucinated turns.

**Answer: B**
**Explanation:** Grounding and multi-step verification such as forcing the model to cite or output raw source material first significantly minimize the risk of fabrication. Forcing the agent to log the source data ensures its context is strictly anchored to real facts before it synthesizes an answer.


---

## Question 9
**Question:** A engineer wants Claude Code to ignore all files ending in .log and all files in the build/ directory. Which .claudeignore content is correct?

* **A) .log and build/ each on their own separate line**
* B) CLAUDE_EXCLUDE: build/, .log
* C) ignore .log, build/
* D) NO_READ: [.log, build/]

**Answer: A**
**Explanation:** The .claudeignore file utilizes standard globbing and structural directory patterns identical to a traditional .gitignore file. To ignore files by extension or exclude a directory entirely each pattern must be placed on its own line. Syntaxes involving custom prefix keys or comma-separated list formatting are entirely unsupported.


---

## Question 10
**Question:** You are building a research agent that needs to summarize 50 different 10-page documents. What is the most cost-effective and efficient way to process this with Claude?

* A) Create 50 separate threads in real-time to get the summaries faster.
* B) Use a single long conversation and append each document one by one.
* C) Use Prompt Caching for each document.
* **D) Use the Message Batches API to process all 50 summarization requests in parallel with a 50% discount.**

**Answer: D**
**Explanation:** The Message Batches API is the standard choice for bulk non-latency-sensitive processing like large-scale summarization offering up to a 50% cost reduction. Appending documents sequentially in a single thread scales costs quadratically since you repeatedly pay for previously processed text.


---

## Question 11
**Question:** A engineer is using Chain of Thought prompting to improve Claude reasoning on a logic puzzle. They notice the thinking is correct but the final answer is wrong. What is the likely fix?

* A) Remove the Chain of Thought instructions.
* B) Use a smaller model to reduce the complexity of the thinking.
* **C) Add Check your work at the end of your reasoning to the prompt instructions.**
* D) Raise the temperature to 1.0.

**Answer: C**
**Explanation:** When a model maps out a flawless chain of logic but stumbles during the final synthesis it is usually a breakdown in closing execution. Explicitly instructing the model to review its own steps right before delivering its final answer bridges the gap between the internal reasoning path and the final text generation.


---

## Question 12
**Question:** An agentic workflow designed for customer returns is failing because the model occasionally calls the refund tool twice for the same order. What is the best architectural safeguard?

* A) Add Never call refund twice to the system prompt in bold letters.
* **B) Make the refund tool idempotent by requiring a unique transaction ID generated per session.**
* C) Raise the reasoning budget for the model to think before calling tools.
* D) Use a lower temperature 0.0 to make the agent behavior more predictable.

**Answer: B**
**Explanation:** State-changing tools in agentic systems must be designed for idempotency to prevent accidental duplication. Idempotency ensures that even if a tool is called multiple times with the same identifier the side-effect or financial transaction occurs exactly once. Prompt constraints can still be overridden in complex edge cases.


---

## Question 13
**Question:** An architect is designing an MCP server to provide real-time inventory data from a legacy SQL database. The LLM occasionally attempts to join too many tables causing timeout errors. What is the most resilient tool design to prevent this?

* A) Raise the timeout duration on the MCP server to 60 seconds.
* **B) Refactor the MCP tool to accept only a single Product_ID and return pre-joined view data rather than allowing raw SQL generation.**
* C) Enable Prompt Caching for the database schema to help the model reason better.
* D) Add Do not perform complex joins to the tool description field.

**Answer: B**
**Explanation:** Constraining tool inputs and returning structured views is a core principle of reliable tool design for agentic systems. Hard-coded or heavily constrained tool parameters prevent the model from creating complex unoptimized queries that cause timeouts. Relying on prompt-based constraints is less reliable than structural constraints in the tool input schema.


---

## Question 14
**Question:** Claude Code is being used on a project with a tests/ directory that contains very large data files. How can you prevent Claude from reading these specific data files while still allowing it to run the tests?

* A) Use the --no-context flag when starting the CLI.
* B) Add the file paths to CLAUDE.md under a Do Not Read section.
* **C) Add tests/*.dat to the .claudeignore file.**
* D) Delete the data files before starting Claude Code.

**Answer: C**
**Explanation:** The .claudeignore file acts as a strict programmatic boundary that completely prevents Claude Code from reading indexing or pulling specified file contents into its context window. Crucially because it only blocks the agent file-system tools from reading the files the files remain physically present on the disk allowing test execution commands to use them perfectly.


---

## Question 15
**Question:** A customer support bot uses the Messages API. The architect notices that the User is frequently interrupted by the bot before finishing their thought. Which parameter or feature should be adjusted?

* A) Decrease the temperature to 0.0.
* **B) Build a client-side Debounce or Message Collector logic before calling the API.**
* C) Use a stop_sequence like User: to tell the model to wait.
* D) Raise the max_tokens parameter to 4000.

**Answer: B**
**Explanation:** Managing the flow of conversation or handling pacing in a UI/UX context is a wrapper-level client-side orchestration responsibility rather than a model-level parameter. The API is stateless per request. It cannot inherently know if a user has stopped typing or is just pausing. Implementing a debounce mechanism on the client side ensures that the system waits for a sustained pause in user input before firing the final API payload.


---

## Question 16
**Question:** In an agentic workflow what is Task Decomposition?

* A) Breaking a large file into smaller chunks for RAG indexing.
* B) The process of deleting old tasks from the database to save space.
* C) Reducing the max_tokens limit to force the model to be more concise.
* **D) The process where a coordinator agent breaks down a complex user request into smaller manageable sub-tasks for itself or subagents.**

**Answer: D**
**Explanation:** Decomposition is a foundational architectural pattern in orchestration. Complex goals often fail when given to an LLM in a single pass. By breaking a large request down into sequential or parallel sub-tasks a coordinator agent can distribute focused workloads to specialized subagents vastly improving planning and reliability.


---

## Question 17
**Question:** A engineer wants to use Claude to extract data from 5000 scanned invoices. They have the images as JPEGs. What is the most cost-effective architecture?

* A) Convert the JPEGs to text using an OCR service first then use a smaller model.
* **B) Use the Message Batches API to process all images in bulk as it offers a 50% discount on token costs.**
* C) Use Prompt Caching for each image.
* D) Process them sequentially using a single real-time API connection.

**Answer: B**
**Explanation:** For high-volume asynchronous document processing workloads like extracting data from thousands of invoices the Message Batches API is the standard architectural recommendation because it provides a straight 50% discount on token costs. Real-time sequential processing is both significantly slower and hits full-price endpoints.


---

## Question 18
**Question:** When using Claude Code what is the Plan Mode primarily used for?

* A) Generating a Gantt chart of the project milestones.
* **B) Allowing the user to review the agent proposed sequence of actions before any tools like file writes are executed.**
* C) Switching the model from Sonnet to Haiku to save money.
* D) Setting a max_tokens limit for the next 24 hours.

**Answer: B**
**Explanation:** Plan mode is a core human-in-the-loop safety feature in Claude Code. It acts as a manual approval gate for complex multi-step engineering tasks allowing you to audit the agent intent strategy and proposed tool modifications before it executes any changes on your local environment.


---

## Question 19
**Question:** What is the role of the Server Discovery phase in the Model Context Protocol MCP?

* **A) It is not a formal protocol phase. Clients are manually configured with server connection details like an executable path or SSE URL.**
* B) It is a security handshake where the server validates the LLM API key.
* C) It is a broadcast signal that allows MCP servers to find any available LLM on the network.
* D) It is a process where the LLM automatically scans the user hard drive for .mcp files.

**Answer: A**
**Explanation:** The Model Context Protocol does not include an automatic network-wide or file-system-wide server discovery mechanism. Instead connection establishment relies entirely on explicit client-side configuration. The client application is manually provided with the direct paths executable commands or SSE endpoint URLs required to launch or connect to each specific MCP server.


---

## Question 20
**Question:** A engineer wants to use Claude to generate a complex Kubernetes manifest. The model keeps making small syntax errors. Which prompt engineering technique is most likely to resolve this?

* A) Tell the model This is very important for my job.
* B) Ask the model to Be a Kubernetes Expert and use Chain of Thought.
* **C) Provide 3-5 few-shot examples of valid Kubernetes manifests in the system prompt.**
* D) Raise the temperature to 0.7 to allow for more creative manifest designs.

**Answer: C**
**Explanation:** Few-shot prompting is highly effective at teaching a model specific syntax requirements structural rules and formatting patterns for highly structured technical outputs. Raising the temperature actually raises the risk of syntax errors by introducing unnecessary randomness.


---

## Question 21
**Question:** You are building a multi-agent research system where a coordinator agent delegates to subagents for web search and document analysis. The synthesis subagent is failing to provide citations for its findings even though the coordinator system prompt explicitly requires them. What is the most likely cause?

* **A) The coordinator forgot to pass the require citations instruction to the synthesis subagent.**
* B) The coordinator is using the Task tool with incorrect parameters.
* C) The web search subagent is not returning source URLs in its output.
* D) The synthesis subagent allowedTools list does not include the Citation tool.

**Answer: A**
**Explanation:** Subagents operate with completely isolated context windows. They do not automatically inherit the parent coordinator system prompts global instructions or history. If a subagent needs to follow a specific constraint like providing citations that constraint must be explicitly passed to it by the coordinator within its own dedicated prompt or task instructions.


---

## Question 22
**Question:** A engineer is using the Batch API for a project. They notice a 400 error for one of the requests in the batch. What happens to the other 499 requests in that same batch?

* A) The entire batch is cancelled immediately and must be resubmitted.
* B) The batch is paused and the engineer has 1 hour to fix the error before it continues.
* **C) The other requests are processed normally. The Batch API processes each request independently within the batch.**
* D) The error is ignored and the model guesses the answer for that specific request.

**Answer: C**
**Explanation:** The Batch API is designed for high-volume asynchronous resilience. Individual failures or malformed requests within a batch do not halt or invalidate the remaining valid items. Each request is evaluated completely independently while failed queries are flagged individually in the final output file.


---

## Question 23
**Question:** You are processing 10000 legal contracts for Entity Extraction using the Message Batches API. You receive a 429 Too Many Requests error when trying to create the batch. What should you do?

* **A) Build an exponential backoff retry logic for the batch creation request.**
* B) Switch to a smaller model as it has higher rate limits.
* C) Delete all previous batches to clear your quota.
* D) Reduce the number of items in the batch to 10.

**Answer: A**
**Explanation:** A 429 Too Many Requests error when attempting to create a batch indicates that the batch management endpoint itself is currently rate-limited rather than the underlying token quota. The correct and robust engineering practice is to build client-side exponential backoff retry logic. Reducing the batch size to 10 defeats the purpose of the Batch API.


---

## Question 24
**Question:** Which feature of Claude is specifically designed to help the model solve complex mathematical and logical problems by allowing it to think step-by-step before answering?

* A) Prompt Caching
* B) JSON Mode
* C) Message Batches API
* **D) Extended Thinking**

**Answer: D**
**Explanation:** Extended Thinking provides a dedicated reasoning space that improves performance on complex tasks. Prompt Caching improves speed and cost but does not change the model underlying reasoning capacity. JSON mode is for structural formatting rather than improving logical reasoning depth.


---

## Question 25
**Question:** In Claude Code you have a .claudeignore file that includes node_modules/. However you want the agent to be able to read the package.json file inside a specific module for dependency checking. How can you achieve this?

* A) Use CLAUDE.md to provide the content of the package.json as a hard-coded string.
* B) Move the package.json file to the root directory temporarily.
* **C) Add an exception rule to .claudeignore using the ! prefix such as !node_modules/special-pkg/package.json.**
* D) Delete .claudeignore and use a system prompt to tell the agent what to avoid.

**Answer: C**
**Explanation:** The .claudeignore file uses standard glob matching patterns identical to .gitignore. To allow or include a specific file or folder that was previously blocked by a broader ignore pattern you prefix the path with an exclamation mark. Removing the entire ignore file reduces tool execution reliability and unnecessarily inflates token usage.


---

## Question 26
**Question:** Which of these is NOT a valid field in an MCP Tool definition?

* **A) max_tokens_per_call**
* B) description
* C) input_schema
* D) name

**Answer: A**
**Explanation:** The Model Context Protocol specification dictates that a tool definition must consist of a name a description and an input_schema. Execution or resource constraints such as limiting tokens are managed externally by the client application rather than being embedded inside the tool interface definition itself.


---

## Question 27
**Question:** You are extracting data from hundreds of resumes. Some resumes are in PDF format and others are images. How should you optimize your API usage to handle both formats efficiently while ensuring structured JSON output?

* **A) Pass the document content to Claude using the tool_use parameter with a strictly defined JSON schema.**
* B) Convert all documents to raw text using OCR first then send the text to Claude.
* C) Use the thinking parameter to have Claude describe the resume first then extract the data.
* D) Use the Batch API with a simple text-based prompt asking for CSV format.

**Answer: A**
**Explanation:** JSON schema configuration via tool_use is the most reliable method for enforcing structured data extraction in production across multi-modal inputs. Because Claude has native vision capabilities it can parse both structural PDFs and raw images directly eliminating the need for a complex pre-processing OCR pipeline.


---

## Question 28
**Question:** You are building an agent that can delete files. How do you implement a Safety Guardrail that prevents it from deleting any file that does not belong to the current user?

* A) Use the .claudeignore file to list all other users files.
* B) Ask the model Is this your file before every delete call.
* C) Add Only delete your own files to the system prompt.
* **D) Check the file ownership metadata in the tool execution code on the server side before calling the delete function.**

**Answer: D**
**Explanation:** Security and authorization boundaries must always be enforced programmatically at the tool or API level server-side never solely via LLM instructions. Prompt instructions or conversational verification steps are probabilistic and can be bypassed by complex adversarial user inputs.


---

## Question 29
**Question:** An architect is designing a RAG system. They want to use Prompt Caching to save costs on the 50000-token knowledge base. Where should the knowledge base be placed in the message array?

* A) After the user latest query to ensure it is the most relevant.
* **B) At the very beginning of the system prompt or the first user message marked with cache_control.**
* C) At the end of the assistant previous response.
* D) In a separate developer role message.

**Answer: B**
**Explanation:** Prompt caching operates on a strict prefix-matching mechanism. Large static chunks of data such as a RAG knowledge base should always be anchored at the very beginning of the message construction chain and tagged with a cache_control breakpoint. Placing it after a dynamic element like a changing user query will break the prefix stability invalidating the cache.


---

## Question 30
**Question:** When implementing an MCP server that manages a local file system which security measure is MOST critical to prevent a Path Traversal attack where an agent might access files outside the project directory?

* **A) Sanitize all input paths by resolving them to their absolute path and checking if they start with the allowed root directory.**
* B) Configure the MCP transport to use stdio instead of SSE.
* C) Use a .claudeignore file to list all folders on the machine.
* D) Add Stay within the current directory to the MCP tool description.

**Answer: A**
**Explanation:** Strict path validation at the server level is the only way to ensure the agent stays within its intended sandbox. Server-side validation is required for security. Models can ignore prompt instructions under pressure and a .claudeignore file is impractical for listing an entire machine directories.


---

## Question 31
**Question:** When implementing a Human-in-the-Loop pattern for a high-value payment agent at which point should the system escalate to a human?

* A) After every single tool call to ensure 100% accuracy.
* **B) When the model identifies a policy gap or when the confidence score for a proposed action is below a certain threshold.**
* C) When the API returns a 500 error code.
* D) Only when the model explicitly says I need help.

**Answer: B**
**Explanation:** Effective HITL design uses confidence thresholds and policy-based triggers to balance autonomy and safety. Relying solely on the model to declare it needs help is unsafe because models can hallucinate confidence even when incorrect.


---

## Question 32
**Question:** When configuring Claude Code for a team environment you want to ensure everyone uses the same pre-commit hook that runs linting before Claude is allowed to merge code. Where should this be defined?

* A) In the CLAUDE.md file as a set of written instructions.
* **B) In the project standard .git/hooks/pre-commit file or configured via .claude/settings.json.**
* C) Adjust the max_tokens parameter to selectively block specific git operations like merging.
* D) In each engineer local shell profile such as ~/.zshrc or ~/.bashrc.

**Answer: B**
**Explanation:** Claude Code natively respects standard Git hooks configured within the repository and allows team-wide agent behaviors to be managed via .claude/settings.json which can be tracked in version control. Relying on written instructions in CLAUDE.md provides guidance but lacks deterministic enforcement.


---

## Question 33
**Question:** You are using Prompt Caching for a chat application. A user message is Hello. The system prompt is 500 tokens. Why might you NOT see a cache hit?

* A) The user used a different language such as Spanish.
* B) The temperature was set to 1.0.
* C) The message was sent via the Batch API.
* **D) The total prompt length is below the minimum threshold for caching currently 1024 tokens for Sonnet and Haiku.**

**Answer: D**
**Explanation:** Anthropic prompt caching enforces a strict minimum token threshold before a prompt segment can be written to or read from the cache. For models like Claude Sonnet and Haiku this baseline requirement is 1024 tokens. Since the combined size of the system prompt and the brief user query falls well short of this threshold it will not trigger the caching mechanism.


---

## Question 34
**Question:** You are building an MCP server that connects to a company Jira instance. To ensure the LLM does not accidentally spam tickets which tool design pattern is BEST?

* **A) Build a Human-in-the-Loop confirmation step in the client application before the MCP tool call is executed.**
* B) Change the MCP transport from stdio to SSE.
* C) Use a system prompt that says Never create more than one ticket per hour.
* D) Set max_tokens to a low value for the create_ticket tool.

**Answer: A**
**Explanation:** Critical destructive or external state-changing actions should always be guarded by a deterministic safety gate which typically involves human verification. Relying on a system prompt is probabilistic and susceptible to model confusion. Modifying transport protocols provides zero logical safety restrictions over execution logic.


---

## Question 35
**Question:** What is the primary benefit of using the Model Context Protocol MCP Resources feature for providing database documentation to an LLM?

* A) Resources automatically encrypt all data before sending it to the LLM.
* B) Resources bypass the token limit by using a special compression algorithm.
* C) Resources allow the LLM to execute SQL queries directly against the database.
* **D) Resources allow the LLM to access data in a standardized read-only format without the engineer needing to manually paste it into the prompt.**

**Answer: D**
**Explanation:** Resources act as a standardized read-only data source within the Model Context Protocol allowing an LLM to programmatically pull in context files or documentation on-demand without manual user intervention or cluttering the initial prompt. Resources still consume standard context window tokens when read.


---

## Question 36
**Question:** An agent needs to extract data from a very long messy transcript. Which strategy minimizes hallucinations where the model might invent data that is not in the text?

* A) Raise the temperature to 0.9 to encourage more diverse extraction.
* B) Tell the model I will tip you $20 for a perfect answer.
* C) Use a few-shot prompt that contains fake data to show the model how to be creative.
* **D) Ask the model to extract quotes supporting every piece of data it finds.**

**Answer: D**
**Explanation:** Requiring explicit citations or direct quote extraction forces the model to ground its outputs strictly within the provided text which dramatically reduces structural fabrications and hallucinations. High temperature settings introduce generation randomness that increases error rates.


---

## Question 37
**Question:** You are building a Code Reviewer agent. You want to ensure it only reviews files that have changed in the last Git commit. Which tool should the agent use?

* A) A Search tool that looks for the string TODO in all files.
* B) The read_file tool with a wildcard like *.
* C) The ls tool to list all files and then the cat tool to read every file.
* **D) A custom tool that executes git diff --name-only HEAD~1 HEAD.**

**Answer: D**
**Explanation:** Using standard command-line interfaces or version control tools via an MCP execution interface is the most direct deterministic and efficient way to gather environment and project state. Manually listing and reading every single file in the repository scales horribly and wastes massive amounts of context window tokens on entirely unchanged source code.


---

## Question 38
**Question:** When implementing an MCP server in Python which library is typically used to handle the JSON-RPC communication and protocol state?

* **A) The official mcp Python SDK.**
* B) Pytest.
* C) Flask or FastAPI.
* D) Requests.

**Answer: A**
**Explanation:** Anthropic provides official SDKs in both Python and TypeScript that natively handle the underlying JSON-RPC 2.0 protocol specifications lifecycle messages and state management for the Model Context Protocol. While frameworks like Flask or FastAPI can host an SSE transport layer they do not inherently understand MCP protocol logic.


---

## Question 39
**Question:** A engineer wants Claude Code to always run npm run lint before every git commit it makes. Where should this instruction be placed for the most reliable enforcement?

* A) In the user ~/.bashrc file.
* B) In the system prompt provided to Claude via the CLI.
* C) In the CLAUDE.md file as a Rule.
* **D) In a project-level pre-commit git hook that the engineer configures in the repository.**

**Answer: D**
**Explanation:** Standard git hooks are the most reliable way to enforce quality boundaries because they run programmatically at the git level blocking any commit that fails the script regardless of whether it was initiated by a human or an agent like Claude Code. While writing instructions in CLAUDE.md is excellent practice it acts as a soft rule rather than a deterministic enforcement mechanism.


---

## Question 40
**Question:** In Claude Code where are project-specific custom slash commands also known as skills defined?

* A) CLAUDE.md
* **B) In Markdown files within the .claude/skills/ or .claude/commands/ directory.**
* C) package.json
* D) .clauderc

**Answer: B**
**Explanation:** Custom workflows and slash commands in Claude Code are implemented as Skills and stored as Markdown files inside the project .claude/skills/ or .claude/commands/ directory. While CLAUDE.md is the central file for general project instructions it does not host custom executable skills.


---

## Question 41
**Question:** A multi-agent system uses a Refining subagent to check the work of a Drafting subagent. The Architect notices the Refining agent is providing generic feedback like looks good instead of detailed critiques. What is the most effective fix?

* A) Enable Extended Thinking for the Drafting agent only.
* **B) Provide the Refining agent with a specific rubric or checklist to use for evaluation in its system prompt.**
* C) Raise the temperature of the Refining agent to 1.0.
* D) Use a larger model for the Drafting agent and a smaller one for Refining.

**Answer: B**
**Explanation:** Multi-pass review architectures require explicit rubrics to direct the reviewing model attention to granular details. Without defined evaluation criteria a model defaults to surface-level patterns yielding shallow approval phrases. Adjusting model sizing or reasoning settings on the Drafting agent does not improve the Refining agent critique quality.


---

## Question 42
**Question:** **Question 1**

* **A) The coordinator should analyze the error report it to the user and proceed with the results from the other 4 subagents if possible.**
* B) The coordinator should immediately terminate all other subagents to save tokens.
* C) The coordinator should retry the failed subagent 50 times in a loop.
* D) The coordinator should ignore the error and hallucinate a successful result for the failed subagent.

**Answer: A**
**Explanation:** Reliable agentic systems must be designed to handle partial failures gracefully. By analyzing the error and proceeding with the remaining successful subagent workloads where independent the system minimizes waste and maintains operational utility instead of crashing completely or executing endless costly retries.


---

## Question 43
**Question:** Which parameter in the Messages API is used to force the model to use a specific tool regardless of what the user asks?

* A) system: You must use the tool my_specific_tool
* B) tool_use: required
* C) forced_tool: my_specific_tool
* **D) tool_choice: { type: tool, name: my_specific_tool }**

**Answer: D**
**Explanation:** The tool_choice parameter provides deterministic hard API-level control over tool execution. By setting the type to tool and providing the exact name you mandate that Claude must invoke that specific tool next. System prompt instructions are soft constraints that can be bypassed and forced_tool is an invalid parameter.


---

## Question 44
**Question:** A structured data extraction pipeline is processing thousands of medical invoices. Some invoices contain hand-written notes that cause the model to occasionally produce malformed JSON. Which strategy provides the best balance of reliability and efficiency?

* A) Raise the max_tokens parameter to ensure the model has enough space to finish the JSON.
* **B) Build a validation-retry loop that catches JSON errors and sends the error message back to the model for correction.**
* C) Switch to a smaller faster model for the extraction to reduce the cost of failures.
* D) Manually review every invoice that contains hand-written notes before processing.

**Answer: B**
**Explanation:** Validation-retry loops with explicit error feedback allow models to self-correct which is an industry-standard architectural pattern for high-fidelity structured data extraction. Smaller models are typically less capable at complex parsing and would likely raise the error rate.


---

## Question 45
**Question:** In the Model Context Protocol MCP what is Transport?

* **A) The underlying communication layer like stdio or SSE that carries JSON-RPC messages between the client and server.**
* B) The process of converting Python code to JavaScript for browser execution.
* C) A security feature that encrypts data during the batch processing phase.
* D) A tool that allows the LLM to move files from one server to another.

**Answer: A**
**Explanation:** In the Model Context Protocol architecture transport refers strictly to the network or system communication layer responsible for moving data back and forth between clients and servers. MCP is designed to be transport-agnostic meaning the higher-level application protocol remains identical whether it runs over local stdio streams or web-based SSE.


---

## Question 46
**Question:** When a model invokes a tool but the tool execution fails with an error how should the error be reported back to the model in the Messages API?

* A) Set max_tokens to 0 for the subsequent turn to signal a failure.
* **B) Add a user role message to the conversation history containing a tool_result block where is_error is set to true.**
* C) Throw a 500 Internal Server Error from the client back to the Anthropic API.
* D) Tell the model Try again in the system prompt.

**Answer: B**
**Explanation:** To allow an agent to gracefully recover from a runtime tool issue errors must be fed back directly into the conversation stream so the model can interpret the failure and decide on a correction strategy. In the Messages API this is done by appending a user role message containing a tool_result block with the is_error flag set to true along with the error text.


---

## Question 47
**Question:** A engineer wants to implement a multi-agent system where a Planner agent creates a JSON list of tasks for a Worker agent. Which pattern is most effective for ensuring the Worker follows the JSON exactly?

* A) Tell the Worker You are a JSON parser in the system prompt.
* **B) Enforce the JSON structure using tool_use with a predefined JSON schema on the Worker agent.**
* C) Use Extended Thinking to help the Worker understand the JSON better.
* D) Set temperature to 1.0 to ensure the Worker is flexible.

**Answer: B**
**Explanation:** JSON schemas configured via tool use provide the strongest structural guarantees for data exchange and instruction following in production workloads. Higher temperatures increase the risk of the model deviating from strict formats and persona prompts are soft constraints that are less reliable than schema enforcement.


---

## Question 48
**Question:** When using the Model Context Protocol MCP with stdio transport how does the client communicate with the server?

* A) The client sends HTTP POST requests to a local port such as 8080.
* B) The client and server communicate via a shared SQLite database.
* C) The client writes a file to disk that the server polls every 5 seconds.
* **D) The client spawns the server as a child process and uses standard input/output streams for JSON-RPC messages.**

**Answer: D**
**Explanation:** stdio transport is the default and most common communication mechanism for local MCP servers. Under this paradigm the host client directly spawns the server executable as a managed child sub-process establishing a dedicated low-latency pipe where structured JSON-RPC 2.0 messages are multiplexed directly across standard input and standard output streams.


---

## Question 49
**Question:** Production data shows that in 12% of cases your agent skips get_customer entirely and calls lookup_order using only the customer stated name occasionally leading to misidentified accounts. What change would most effectively address this reliability issue?

* **A) Add a programmatic prerequisite such as middleware or validation gates that blocks lookup_order and process_refund calls until get_customer has returned a verified customer ID.**
* B) Enhance the system prompt to state in bold letters that customer verification via get_customer is mandatory before any order operations.
* C) Build a routing classifier that analyzes each request and enables only the subset of tools appropriate for that request type.
* D) Add few-shot examples showing the agent always calling get_customer first.

**Answer: A**
**Explanation:** Programmatic enforcement through prerequisite gates or backend validation is the most effective way to guarantee deterministic compliance for critical workflow steps like identity verification. Prompt-based guidance and few-shot examples are probabilistic interventions. The model can still occasionally skip steps under complex or edge-case user inputs.


---

## Question 50
**Question:** You are designing a coding agent that needs to work across a mono-repo with millions of lines of code. How should the agent find the relevant files to edit?

* A) Use the Batch API to index the repository every time the agent starts.
* B) Ask the user to provide the exact file paths for every single turn.
* **C) Build a multi-step Explore-then-Act loop where the agent first uses search tools like grep or ripgrep to identify relevant files.**
* D) Load the entire mono-repo file tree into the system prompt.

**Answer: C**
**Explanation:** For massive codebases loading the entire file tree is completely unfeasible due to context window saturation and extreme inefficiency. The standard architectural pattern for navigating vast file systems is an Explore-then-Act loop where the coordinator agent uses high-performance search utilities to autonomously scan code patterns and target the precise files requiring modification before executing any writes.


---

## Question 51
**Question:** A financial analyst is using Claude to summarize a 200-page regulatory filing. The model response is often cut off mid-sentence. Which API parameter adjustment is most likely to resolve this?

* A) Enable Extended Thinking with a 2000 token budget.
* **B) Raise max_tokens to its maximum limit such as 4096 or 8192.**
* C) Add summarize the whole document to the user prompt.
* D) Decrease temperature to 0.0.

**Answer: B**
**Explanation:** When a response is cut off mid-sentence it typically indicates that the generation reached the hard token ceiling specified by the max_tokens parameter for that single turn. Raising max_tokens to its maximum limit gives the model the necessary headroom to complete long summaries.


---

## Question 52
**Question:** A engineer is using the Claude Agent SDK and wants to persist the agent state across different user sessions. What is the recommended approach?

* **A) The engineer must implement a custom storage layer such as SQLite or Redis to save and load the message history and pass it to the agent at the start of each session.**
* B) Set persistent: true in the agent configuration object.
* C) The agent automatically saves its memory to a .memory.json file in the root directory.
* D) Use Prompt Caching to store the session data indefinitely.

**Answer: A**
**Explanation:** Statelessness is a core design principle of the Claude API. Application state and session memory must be managed externally. There is no persistent flag in the stateless API or standard SDK configurations. Prompt Caching is ephemeral and designed to save costs on static context not for long-term session persistence.


---

## Question 53
**Question:** In the Messages API what happens if you set the thinking budget to be larger than the max_tokens value?

* A) The thinking tokens will not be charged to the user.
* **B) The API will return a validation error 400 Bad Request.**
* C) The model will ignore the max_tokens limit and prioritize thinking.
* D) The thinking budget will be automatically reduced to match max_tokens.

**Answer: B**
**Explanation:** The max_tokens parameter acts as a strict global ceiling for the entire response turn encompassing both internal reasoning tokens and the final visible output tokens. Because the thinking budget cannot logically exceed the total token limit the API will reject the setup immediately with a validation error.


---

## Question 54
**Question:** Your application uses Claude for code generation. Users report that the model sometimes produces very long Internal Monologue that delays the actual code output. What is the most effective way to address this for a low-latency UI?

* **A) Stream the response and display the thinking content in a collapsible UI element as it arrives.**
* B) Disable the thinking parameter entirely to speed up the response.
* C) Use a smaller model like Claude Haiku for all code generation tasks.
* D) Set the budget_tokens to the lowest possible value such as 1024.

**Answer: A**
**Explanation:** Streaming allows the client UI to receive content progressively reducing time-to-first-token and perceived latency. By rendering the thinking content inside a collapsible container as it streams in users can track the model progress dynamically without waiting for the entire generation to complete. Disabling thinking altogether significantly risks degrading code accuracy on complex tasks.


---

## Question 55
**Question:** In an MCP server what is the purpose of the resources concept compared to tools?

* **A) Resources provide read-only data like a documentation file or log while tools are for taking actions like writing a file.**
* B) Resources allow the LLM to call other LLMs while tools are for local code execution.
* C) Resources are only for image files while tools are for text-based tasks.
* D) Resources are used to manage API keys while tools manage function calls.

**Answer: A**
**Explanation:** In the Model Context Protocol the distinction between resources and tools comes down to read-only data access versus active execution capabilities. Resources act as standardized read-only data sources that provide background context to the model. Tools on the other hand represent executable capabilities that allow the model to take actions manipulate states or perform side-effect operations.


---

## Question 56
**Question:** A engineer wants to ensure that Claude Code always follows a specific naming convention for new files such as kebab-case. Where is the BEST place to define this rule?

* A) By creating a dummy file named kebab-case-example.txt.
* **B) In the project CLAUDE.md file under a Code Style or Naming Conventions section.**
* C) In a .gitignore file.
* D) In the user shell history.

**Answer: B**
**Explanation:** CLAUDE.md is the authoritative initialization and rule file that Claude Code checks in the project root for development conventions code style guides and command instructions. Defining your preferred file naming standards here ensures the agent consistently adheres to them during the session.


---

## Question 57
**Question:** A engineer wants to use Extended Thinking for a complex legal analysis task. They need to ensure the final response stays within a strict budget of 4000 total tokens including reasoning. How should they configure the API call?

* A) Only set budget_tokens to 4000. The API will automatically calculate max_tokens.
* **B) Set the thinking object with budget_tokens and ensure max_tokens is set higher than the thinking budget.**
* C) Use the stop_sequences parameter to cut off the generation at exactly 4000 tokens.
* D) Set max_tokens to 4000 and the temperature to 1.0.

**Answer: B**
**Explanation:** When using Extended Thinking the budget_tokens parameter controls the maximum size of the reasoning space while max_tokens dictates the global limit for the complete API response turn. Therefore max_tokens must always be configured to a value strictly greater than the thinking budget to leave enough token headroom for the final answer.


---

## Question 58
**Question:** During a complex multi-agent research task you notice the coordinator agent frequently re-assigns the same sub-topic to different subagents leading to redundant work and high token usage. What is the most likely architectural flaw?

* A) The Task tool does not support parallel execution causing the coordinator to lose track.
* B) The system prompt for the subagents is too long causing them to forget their assignments.
* C) The subagents are not sharing a global memory space to see each other work.
* **D) The coordinator is performing overly narrow task decomposition without tracking progress.**

**Answer: D**
**Explanation:** In an orchestration pattern the coordinator agent is entirely responsible for breaking down the primary goal managing state and partitioning assignments cleanly. If it repeatedly issues overlapping or identical tasks the flaw lies in its internal delegation and state-tracking logic such as not updating its internal scratchpad or checklist when a sub-task is spun up.


---

## Question 59
**Question:** You are implementing Prompt Caching for a financial analysis tool that uses a massive 100k token quarterly report. The user often asks follow-up questions about specific tables. How should you structure the message to maximize cache hits?

* A) Place the user latest question first followed by the quarterly report.
* B) Use the Message Batches API for all queries related to the 100k report.
* C) Send the report as a separate user message with no caching as 100k tokens is too large to cache.
* **D) Place the quarterly report at the beginning of the prompt and mark it with cache_control: type: ephemeral.**

**Answer: D**
**Explanation:** Prompt caching is strictly prefix-based. To maximize cache hits large and stable context blocks such as the 100k token quarterly report must be placed at the very beginning of the message array. Shifting the user highly variable question to the front would invalidate the cache for everything following it.


---

## Question 60
**Question:** When designing a tool for an agent to Write a File what is the most important security check to implement inside the tool backend code?

* A) Ensure the file size is less than 100KB.
* B) Only allow the tool to write files ending in .txt.
* **C) Validate that the target_path is within the allowed project directory and resolve all symlinks to prevent directory traversal.**
* D) Check if the model system prompt includes You are a helpful assistant.

**Answer: C**
**Explanation:** Security boundaries and authorization checks must always be strictly enforced programmatically at the execution layer never via probabilistic model prompt instructions. When giving an agent file-writing capabilities checking and validating the canonical path by resolving symlinks prevents malicious path traversal attacks.


---
