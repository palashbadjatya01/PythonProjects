# CCA Foundations — Practice Exam 6 (60 Questions)

---

## Question 1
**Question:** You are deploying a support agent in a global market where users speak 20 different languages. What is the most cost-effective and architecturally clean way to handle this?

* A) Use a translation API to translate every user message to English and back again.
* B) Deploy 20 different instances of the agent each with a localized system prompt.
* C) Only support English and ask the user to use a browser extension for translation.
* **D) Use a single agent with a system prompt that includes: You are a multilingual assistant. Always respond in the user language.**

**Answer: D**
**Explanation:** Claude models are natively multilingual and trained on a vast corpus of global data allowing them to handle language detection and fluid response execution smoothly within a single session. Relying on this native capability is the most architecturally clean approach because it eliminates the maintenance overhead and complexity of managing 20 separate model instances or localized prompts.


---

## Question 2
**Question:** You are building a support agent that must handle multi-page PDF documentation. Users frequently ask questions that require combining information from page 2 and page 50. Which strategy best ensures the agent can accurately synthesize this information?

* A) Load the entire PDF into a single message and use Prompt Caching.
* B) Instruct the agent to read the entire document carefully before answering.
* C) Use vision to see the document layout.
* **D) Use a Coordinator to segment the document into chapters and delegate synthesis to a subagent that sees a structured summary of each chapter.**

**Answer: D**
**Explanation:** Synthesizing information across massive context windows is subject to attention dilution and the Lost in the Middle effect. Even with large context windows models can struggle to connect data points that are thousands of tokens apart. The architectural solution is recursive summarization or hierarchical context. By breaking a long document into logical segments and having a model generate concise semantic summaries of each you create a map of the document that the Coordinator can reason over to identify which specific segments are relevant to a query.


---

## Question 3
**Question:** You are extracting line items from a complex 50-page invoice. The model frequently misses items on page 25. Which architectural change most effectively improves the recall?

* A) Use Prompt Caching to save money on the large document.
* **B) Split the document into overlapping 5-page chunks and process them in parallel with a synthesis step at the end.**
* C) Switch to a smaller model to process the document faster.
* D) Instruct the model to Be an expert accountant in the system prompt.

**Answer: B**
**Explanation:** The recall penalty of long-context models is an architectural constraint. As the input size grows the model attention resolution for any specific token decreases frequently causing it to miss details in the middle of long inputs known as the Lost in the Middle effect. The most robust architectural solution is recursive decomposition segmenting the 50-page document into smaller overlapping chunks. Processing each chunk independently within a fresh smaller context window ensures maximum attention and high recall for every line item.


---

## Question 4
**Question:** A engineer is using productivity tools to navigate an unfamiliar 5000-file codebase. They need to find all occurrences of a specific internal error code ERR_731 across the entire project. Which built-in tool is most efficient for this task?

* A) Read
* B) Bash
* C) Glob
* **D) Grep**

**Answer: D**
**Explanation:** Efficient codebase navigation requires using high-throughput search tools. In a large project containing thousands of files reading files individually using a Read tool is extremely slow and token-inefficient. The built-in Grep tool is highly specialized for this exact task allowing the agent to scan thousands of files in a single turn and return only the relevant matching lines and filenames. Glob is used for listing files matching a pattern not for searching text patterns inside those files.


---

## Question 5
**Question:** A engineer wants to share a specific Code Review workflow with their entire team using Claude Code. What is the recommended way to distribute this configuration?

* A) Email the instructions to every engineer.
* B) Use the global_config flag in the Claude Code CLI.
* C) Add the instructions to the company internal Wiki.
* **D) Check the .claude/skills/ directory into the project Git repository.**

**Answer: D**
**Explanation:** Treating agent configuration as code is the recommended best practice for collaborative AI engineering. By checking the .claude/ directory which contains skills hooks and project rules directly into your Git repository you ensure that every team member automatically inherits and shares the exact same standardized AI configurations. This layout enables inherited expertise where complex prompt engineering custom commands and specialized tool-use workflows built by an architect are instantly available to every engineer cloning the repository.


---

## Question 6
**Question:** In a multi-agent research system the Synthesis agent is producing reports that lack the specific data found by the Search agent. Investigation shows both agents are being called successfully. What is the most likely architectural flaw?

* **A) The Coordinator is not explicitly passing the Search agent results into the Synthesis agent prompt.**
* B) The Search agent is using Prompt Caching incorrectly.
* C) The Search agent context is too large for the Synthesis agent to read.
* D) The Synthesis agent has a lower temperature setting than the Search agent.

**Answer: A**
**Explanation:** The data propagation pattern is the most critical mental model for multi-agent architects. Because subagents operate in isolated contexts they have no automatic awareness of what other agents have discovered unless that information is explicitly bridged and passed along by the supervising Coordinator agent. If a Synthesis agent fails to incorporate data found by a Search agent it is almost always because the orchestrating Coordinator failed to capture format and inject those findings into the Synthesis agent execution prompt.


---

## Question 7
**Question:** An engineer wants to automate the grunt work of updating the copyright year in the headers of 1000 source files. What is the most token-efficient way for an agent to perform this task?

* A) Use the Write tool to open and edit each file individually.
* **B) Instruct the agent to write a sed script and execute it using the Bash tool.**
* C) Use Prompt Caching to store the contents of all 1000 files.
* D) Upload all 1000 files to the context window and ask for a Refactor response.

**Answer: B**
**Explanation:** The power of the shell is a critical leverage point for agentic engineer tools like Claude Code. When tasked with highly repetitive structural modifications across a large file tree forcing an agent to rewrite files line-by-line is an anti-pattern that triggers high latency extreme token costs and eventual rate-limit exhaustion. The most advanced token-efficient architecture relies on meta-automation. By leveraging a Bash tool execution capability the agent only needs to use a tiny fraction of its context window to write a deterministic shell script and run it. This elegantly collapses a 1000-turn workflow into a single reason-and-execute turn.


---

## Question 8
**Question:** When building a research agent why is it recommended to convert raw HTML from web searches into Markdown before passing it to the model?

* **A) Markdown is more token-efficient than raw HTML.**
* B) Markdown allows for Extended Thinking mode to work better.
* C) HTML is considered unsafe and might trigger a safety filter.
* D) Markdown is the only format Claude can read.

**Answer: A**
**Explanation:** Input data optimization is a core architectural lever for token management. Raw HTML is highly noise-heavy often containing hundreds or thousands of tokens for boilerplate tags embedded scripts and styles that offer zero semantic value for the model reasoning. Converting HTML to clean Markdown preserves the essential structural signal while stripping out formatting overhead frequently reducing the total token count by up to 80%.


---

## Question 9
**Question:** When building a tool for an agent to update_database_record why is it recommended to return the updated record as the tool result?

* A) It prevents tool selection ambiguity in the next turn.
* **B) It allows the agent to verify that its requested changes were applied correctly without making an additional read call.**
* C) It is required by the MCP specification.
* D) It ensures that the entire database is loaded into Claude context.

**Answer: B**
**Explanation:** High-fidelity tool design in agentic workflows relies heavily on tight feedback loops. In complex systems every state-changing action should ideally be self-verifying. By returning the fully updated record or a comprehensive status summary directly as the result of a write operation you allow the agent to immediately confirm that its intent was successfully translated into reality. Without this information return pattern the agent is forced to either assume success which introduces systemic risk or execute a redundant follow-up read call unnecessarily increasing total latency and API costs.


---

## Question 10
**Question:** You want to optimize the cost of extracting data from 100000 resumes. Most resumes are 1-2 pages but some are 20+ pages. Which architectural pattern is most efficient?

* A) Use the Message Batches API for all resumes.
* B) Build Prompt Caching for the resume templates.
* **C) Use a Coordinator to check the page count and route long resumes to Sonnet and short ones to a smaller model.**
* D) Use Claude Sonnet for everything to ensure maximum consistency.

**Answer: C**
**Explanation:** The tiered inference pattern is the key to cost-optimized AI systems. Not all extractions require the reasoning power of Sonnet or Opus. For 100000 resumes a triage agent or coordinator can first analyze the complexity of the document. Resumes that are simple and short can be routed to a smaller cheaper model while complex 20-page CVs are routed to Sonnet. This dynamic routing strategy ensures you only pay for the intelligence you actually need for each specific instance.


---

## Question 11
**Question:** You are building a Legal Discovery system where an agent must find relevant clauses across 10000 documents. To ensure high recall for information located in the middle of long documents which strategy should you use?

* **A) Build a sliding window segmentation strategy where documents are split into overlapping 20-page chunks.**
* B) Instruct the model to be very careful with the middle pages.
* C) Load each full document into the context window for a single pass.
* D) Use the Message Batches API to process the full documents.

**Answer: A**
**Explanation:** Long-context performance in Large Language Models is not completely uniform. Models frequently exhibit the Lost in the Middle effect where they demonstrate significantly higher accuracy and recall when attending to information at the absolute beginning or the very end of their input context window. A sliding window segmentation pattern splits massive text volumes into smaller overlapping chunks guaranteeing that every section of a document eventually occupies a primary context position preventing attention dilution and maximizing total factual recall.


---

## Question 12
**Question:** When refactoring a large legacy repository Claude Code occasionally uses an outdated library that was removed months ago. Why is this happening and how can it be fixed?

* A) The .gitignore file is blocking Claude from seeing the new library.
* **B) The codebase still contains deprecated code examples that Claude is discovering and using as patterns.**
* C) The engineer is using the wrong model version.
* D) Claude internal training data is out of date.

**Answer: B**
**Explanation:** Claude is an in-context learner and heavily internalizes the existing code structure and style of the workspace it is given. In large legacy repositories where an old library has been removed from dependencies but leftover dead code unpruned files or stale documentation examples still exist Claude may discover these outdated blocks and replicate them as valid patterns. To fix this engineers should add an explicit negative constraint in the project CLAUDE.md file or permanently prune the legacy code fragments from the codebase.


---

## Question 13
**Question:** A customer support agent for a bank is designed to handle account issues and billing disputes. The agent must escalate any refund over $200 to a human manager. Which implementation strategy provides the most deterministic guarantee of this business rule?

* **A) Build a tool call interception hook PreToolUse that checks the amount parameter and blocks the call if it exceeds $200.**
* B) Use a smaller faster model to handle the refunds as its faster speed reduces the window for errors.
* C) Add several few-shot examples showing the agent correctly escalating high-value refunds.
* D) Include the $200 limit in the agent system prompt and instruct it to ask for permission.

**Answer: A**
**Explanation:** Deterministic business rules in high-stakes environments like banking should always be enforced through programmatic hooks or prerequisite gates at the tool level rather than relying solely on probabilistic prompt instructions. While Claude is highly capable of following instructions prompt-based limits can be bypassed through creative user inputs or model drift. Implementing a PreToolUse check ensures that the business logic is handled in the application layer providing a 100% guarantee of compliance.


---

## Question 14
**Question:** An architect is designing a pipeline to extract data from 10000 unstructured invoices. The extraction requires high precision but can be processed overnight. Which approach is most cost-effective?

* A) Prompt Caching for each invoice.
* B) Streaming Messages API.
* C) Claude Code with a custom Extractor skill.
* **D) Message Batches API.**

**Answer: D**
**Explanation:** The Message Batches API offers a 50% discount on standard token pricing and a 24-hour turnaround window making it the ideal choice for high-volume non-real-time data extraction tasks. While Claude Code is designed as an interactive engineer productivity agent rather than a bulk data processing engine Prompt Caching offers little benefit here because each unstructured invoice contains unique content that does not result in recurring cache hits.


---

## Question 15
**Question:** You are building an automated Test Generation pipeline using Claude Code. Some generated tests fail because of missing local dependencies. How can you improve the success rate?

* A) Switch to a smaller model to reduce the cost of the failed attempts.
* B) Add more memory to the CI server.
* **C) Build a Retry Loop in your CI script that feeds the test failure error back to Claude Code for a second attempt.**
* D) Raise the model temperature.

**Answer: C**
**Explanation:** Autonomous self-correction loops allow an agent to learn from technical execution errors such as missing imports or syntax discrepancies and resolve them dynamically in a subsequent turn. Designing your script to execute the tests capture the failure logs and feed that diagnostic output back to Claude Code leverages the model ability to self-correct dramatically increasing the final success rate.


---

## Question 16
**Question:** When using Claude Code for a large-scale refactoring task you notice that the model suggestions are starting to become less accurate after 50 turns. Which command should you use to reset the context while preserving the changes made to the codebase?

* A) /reset
* B) /exit followed by a restart.
* **C) /clear**
* D) /compact

**Answer: C**
**Explanation:** As an interactive command-line session grows the accumulating conversation history eventually saturates the model context window. This saturation can lead to reasoning fatigue slower response times or repetitive and increasingly inaccurate suggestions. The built-in Claude Code command /clear is designed specifically to solve this issue. It prunes the context window by clearing out the historical conversation log and resetting it to a clean state crucially without altering the physical files or discarding any code changes you have already made in your repository during that session.


---

## Question 17
**Question:** An architect is designing a system where Claude Code reviews PRs and flags breaking changes. How can the system be tuned to ensure the feedback is actionable for the engineer?

* **A) In the system prompt instruct Claude to Only flag issues where you can provide a code snippet for a fix.**
* B) Tell Claude to be as strict as possible during the review.
* C) Use vision to analyze the PR diff as an image.
* D) Set the temperature to 1.0 to encourage creative solutions.

**Answer: A**
**Explanation:** Actionable feedback is a core prompt engineering design choice. In automated CI reviews the signal-to-noise ratio determines the system success. By mandating a problem-solution coupling in the prompt you transform the AI from a vague critic into a constructive collaborator. High temperature leads to less precise and potentially hallucinated suggestions and extreme strictness typically spikes the false positive rate with minor nitpicks.


---

## Question 18
**Question:** A development team uses Claude Code daily. They want to ensure that every time Claude Code is started in their main repository it automatically understands their project unique testing framework and avoids deprecated APIs. Where should this configuration be stored?

* A) In the project .gitignore file.
* B) As a series of custom slash commands in the user .bashrc.
* **C) In a CLAUDE.md file at the repository root.**
* D) In a global system prompt within the Claude Code CLI settings.

**Answer: C**
**Explanation:** The CLAUDE.md file serves as the foundational context layer for Claude Code. Unlike global settings CLAUDE.md allows for project-specific grounding. It acts as the project Standard Operating Procedures defining everything from the build system and test commands to architectural philosophies and forbidden or deprecated libraries. By keeping this file at the root of the repository and checking it into version control you ensure that every engineer on the team and the AI itself operates from the same single source of truth.


---

## Question 19
**Question:** In a long Claude Code session involving 100+ files you notice the tool is becoming slow and forgetful of the initial project brief. What is the most token-efficient way to restore performance?

* A) Restart the terminal.
* B) Raise the max_tokens setting to 400000.
* **C) Use the /clear command and then provide a concise summary of the current state and goals.**
* D) Switch to a larger model.

**Answer: C**
**Explanation:** Peak performance in agentic sessions requires active context pruning. As the session length increases the context window becomes crowded with previous attempts massive tool results and conversational noise leading to attention dilution. The built-in /clear command is the primary tool for resetting the reasoning engine. By clearing the history you wipe away the noise while keeping the working session active. Providing a concise state summary immediately after clearing ensures the model has the high-level context it needs to continue without wasting tokens or re-reading the entire project history.


---

## Question 20
**Question:** You are building an MCP server that needs to support both local engineers using Claude Desktop and a cloud-based agentic system. Which transport methods should you implement to ensure maximum compatibility?

* A) gRPC and GraphQL.
* B) WebSockets and MQTT.
* C) Binary and Text streams.
* **D) STDIO and HTTP+SSE.**

**Answer: D**
**Explanation:** The Model Context Protocol officially standardizes on two primary transport mechanisms. For local-first configurations such as Claude Desktop or Claude Code running on a engineer machine the protocol uses Standard Input/Output process streams. For distributed remote or cloud-based agent architectures it relies on HTTP with Server-Sent Events. Alternative transport options like gRPC GraphQL WebSockets or custom raw binary streams are not part of the standard core MCP specification.


---

## Question 21
**Question:** In which scenario is plan mode in Claude Code most beneficial for a engineer?

* A) When searching the codebase for a specific string using grep.
* **B) When performing a complex refactor that affects multiple modules and architectural layers.**
* C) When running a single unit test using the bash tool.
* D) When performing a simple one-line bug fix in a single file.

**Answer: B**
**Explanation:** Plan mode is a critical Human-in-the-Loop safety feature designed for destructive or wide-ranging operations. By forcing the AI to outline its step-by-step approach and strategy before executing any file writes or structural tool calls the engineer has an opportunity to audit the reasoning and catch potential side effects. For trivial changes single test executions or non-destructive search queries plan mode adds unnecessary overhead and slows down the interactive development workflow.


---

## Question 22
**Question:** You are creating a productivity tool that allows Claude to search through internal Slack channels. You notice that Claude frequently searches for the same keywords in every turn. How can you optimize this?

* **A) Instruct the agent to maintain a Search_History.md file to track what it has already checked.**
* B) Raise the model temperature to 1.0 to encourage variety.
* C) Disable the search tool after the first use.
* D) Tell the agent to remember what you searched in the system prompt.

**Answer: A**
**Explanation:** Agents are subject to working memory decay. In long-running information-gathering tasks the model can lose track of previous turns leading to redundant tool calls and looping behavior. The externalized state pattern involves giving the agent a dedicated scratchpad or log file to record its progress. By reading its own search history at the start of every turn the agent maintains a definitive record of what has been explored and what remains ensuring the agent remains productive and token-efficient throughout the entire mission.


---

## Question 23
**Question:** A team wants to use Claude Code in CI to automatically generate a Security Review for every PR. They are worried about the high token cost of reading the entire codebase for every change. What is the best optimization?

* A) Use the Message Batches API for the security review.
* B) Switch to a smaller model for the review task.
* **C) Only send the git diff of the PR to Claude Code instead of the full file contents.**
* D) Disable Prompt Caching to save on the Cache Write costs.

**Answer: C**
**Explanation:** Optimizing the context-to-insight ratio is the primary way to manage AI costs in CI/CD pipelines. For a Pull Request the most high-signal information is the delta what has actually changed since the last stable version. By architecting your pipeline to only pass the git diff you reduce the input token volume by orders of magnitude compared to reading the entire repository. While the Batch API is cost-effective it introduces significant turnaround latency making it a bottleneck for real-time blocking CI/CD gates.


---

## Question 24
**Question:** A engineer wants to use Claude Code to automate the generation of API documentation from source code. They want to trigger this specific workflow using a custom /gen-docs command. What is the most efficient way to implement this?

* **A) Create a custom Agent Skill in the .claude/skills/ directory.**
* B) Use a PostToolUse hook to detect when a file is saved and trigger the docs generation.
* C) Create a shell alias in the OS that pipes a prompt to the claude command.
* D) Add the documentation rules to the CLAUDE.md file.

**Answer: A**
**Explanation:** Extending Claude Code through Agent Skills is the primary way to create repeatable expert workflows. While CLAUDE.md provides helpful baseline project context it cannot register brand new interactive slash commands within the CLI interface. Agent Skills allow you to encapsulate complex multi-step prompts and register them as first-class slash commands directly inside the agent environment. By placing these skill definitions in the .claude/skills/ directory and checking them into Git you can standardize documentation testing and refactoring patterns across your entire team.


---

## Question 25
**Question:** You are building a pipeline to extract data from thousands of messy HTML pages. You find that the presence of Navigation Bars and Footers confuses the extraction of the main article. What is the best fix?

* A) Raise the context window to allow for more noise.
* B) Tell Claude to Ignore the navigation bar in the system prompt.
* **C) Use a pre-processing script to strip non-essential HTML tags before sending the text to Claude.**
* D) Use a smaller model as it is faster at reading noise.

**Answer: C**
**Explanation:** The signal-to-noise ratio is the primary driver of extraction accuracy. Raw web data is filled with contextual noise such as ads navigation bars and footers that unnecessarily consume tokens and dilute the model attention. Implementing a pre-filtering layer using lightweight programmatic tools to strip out non-semantic content before it reaches the LLM is the most reliable approach. This optimization significantly reduces token costs decreases processing latency and maximizes the reasoning fidelity of the model.


---

## Question 26
**Question:** When building an MCP tool that returns 10MB of raw log data how should you optimize the response for the agent?

* **A) Build server-side filtering to return only the 100 most relevant log lines or high-signal errors.**
* B) Compress the log data using GZIP before returning it.
* C) Return the full 10MB to ensure no information is lost.
* D) Return the data in 100 separate 100KB chunks.

**Answer: A**
**Explanation:** Maintaining strict context hygiene is a primary architectural responsibility when designing agentic systems. Passing massive unfiltered data structures into the model context window leads to severe attention dilution where the model struggles to locate key details amidst the noise and results in substantially higher token costs and processing latencies. Professional MCP tools should implement edge processing. Rather than dumping raw high-volume payloads into the context window the tool should accept filtering parameters and perform the extraction work directly on the host server.


---

## Question 27
**Question:** An engineer is using the Bash tool to debug a performance issue. They want to ensure Claude does not accidentally kill critical production processes while running top or kill commands. What is the best safety measure?

* A) Ask the engineer to approve every single Bash command manually.
* B) Run Claude in a sandbox environment that has no access to the production network.
* C) Add BE CAREFUL to the system prompt.
* **D) Build a PreToolUse hook that regex-checks the kill command for specific process IDs.**

**Answer: D**
**Explanation:** Safety in engineer productivity tools must be treated as a strict programmatic constraint. While prompting the agent to be careful provides a baseline layer it relies on probabilistic model compliance. Manual approval offers high control but introduces severe approval fatigue. A PreToolUse interceptor hook acts as a deterministic programmatic safeguard that evaluates the exact command arguments before execution guaranteeing a reliable boundary regardless of the model intent.


---

## Question 28
**Question:** When an agent handles a subscription cancellation company policy requires it to offer a 20% discount as a retention offer first. Only if the user declines twice should the cancellation proceed. How should this be implemented?

* A) Set the model stop_sequence to CANCEL to prevent early exits.
* B) Add the retention script to the system prompt and hope the agent follows it.
* **C) Build the retention logic as a programmatic state machine that wraps the cancel_subscription tool.**
* D) Provide 20 few-shot examples of successful retention.

**Answer: C**
**Explanation:** Complex business-critical multi-step processes should not rely solely on probabilistic prompt instructions. Strict guardrails and gatekeeping logic such as tracking the number of times an offer has been rejected must be enforced programmatically. By wrapping sensitive tools in backend code the system guarantees 100% compliance with corporate policy regardless of creative model outputs or user manipulation attempts.


---

## Question 29
**Question:** Your structured data extraction tool is failing because the model occasionally produces malformed JSON when processing hand-written notes. Which strategy provides the most reliable recovery mechanism?

* A) Switch to a smaller model to reduce the cost of failures.
* B) Raise max_tokens to ensure the JSON is not truncated.
* C) Tell the model to be very careful with commas in the system prompt.
* **D) Build a Validation-Retry loop that feeds the JSON error back to the model for correction.**

**Answer: D**
**Explanation:** Production-grade extraction systems must be resilient to malformed output. Even with strict schema enforcement complex or messy inputs can occasionally lead to JSON syntax errors. The Validation-Retry Pattern is the industry standard for handling these edge cases. When a JSON error is detected the system catches the exception and initiates a secondary turn sending the malformed JSON along with the specific error message back to the model. This feedback allows the model to focus its reasoning directly on the syntax error and provide a corrected version.


---

## Question 30
**Question:** A research agent needs to summarize 50 academic papers. You use Prompt Caching to store the papers contents. Which statement best describes the cost implications of this architecture?

* A) Caching is automatically applied and does not change the billing model.
* B) Caching reduces the cost of both input and output tokens by 50%.
* C) Caching is only cost-effective for contexts under 5000 tokens.
* **D) The first write turn to the cache is more expensive than standard input but subsequent hits are up to 90% cheaper.**

**Answer: D**
**Explanation:** Prompt Caching introduces an asymmetric pricing model designed to reward structural persistence over multi-turn interactions. A cache write the initial token parsing and storage incurs a premium penalty typically around 25% higher than standard input baseline fees. However subsequent read hits from that preserved cache block provide massive discounts up to 90% cheaper. This economic optimization is highly efficient for heavy-context scenarios like querying a collection of 50 academic papers across multiple investigative turns.


---

## Question 31
**Question:** You are building a multi-agent system where a Coordinator agent delegates billing disputes to a specialized Billing subagent. During testing the subagent fails to resolve a dispute because it cannot see the customer VIP status even though the Coordinator mentioned it in the initial turn. What is the fundamental cause?

* A) The Coordinator used the wrong JSON schema for the subagent tool call.
* B) The subagent allowedTools list did not include the get_customer_status tool.
* **C) Subagents operate with isolated context and do not inherit the history or system prompt of the Coordinator.**
* D) The Coordinator system prompt was too long causing it to forget the VIP status.

**Answer: C**
**Explanation:** In advanced agentic architectures context isolation is a core principle. Subagents do not automatically inherit the conversation history system prompt or tool results of the parent Coordinator agent. As an architect you must ensure that the Coordinator explicitly extracts and passes all relevant data points such as customer status account IDs or previous decisions into the subagent initialization prompt.


---

## Question 32
**Question:** **Question 1**

* A) Ask the user to fix the website API before continuing.
* **B) Catch the error from the Search subagent and re-task it to use an alternative tool or data source.**
* C) Immediately terminate the entire session and return an error to the user.
* D) Use its internal reasoning to hallucinate plausible data to fill the gap.

**Answer: B**
**Explanation:** Professional agent architecture requires graceful failure recovery. In a multi-agent system the failure of a single subagent should not crash the entire mission. A robust Coordinator agent should be prompted with fallback strategies. If a primary tool call returns an error the Coordinator should detect this in the tool output and attempt to re-route the task using a different data source.


---

## Question 33
**Question:** A engineer wants to ensure that Claude Code automated PR feedback is posted directly as comments on the GitHub Pull Request. What is the best architectural approach?

* **A) Use the --output-format json flag and a separate script that pipes the JSON results to the GitHub PR Comments API.**
* B) Claude Code natively supports posting to GitHub via the --github flag.
* C) Instruct Claude to log in to GitHub and post the comment itself.
* D) Give Claude Code the write permission to the .git directory.

**Answer: A**
**Explanation:** Professional CI/CD architectures follow the decoupling principle. A more robust and secure pattern is to have the AI perform the reasoning and analysis and output its findings in a structured format like JSON. A separate lightweight automation script or platform utility then reads that structured data and handles the platform-specific integration using official APIs and tokens. This separation of concerns simplifies testing isolates credentials and ensures your workflow is not entirely dependent on a single CLI tool native integrations.


---

## Question 34
**Question:** A engineer is using Claude Code to build a new React application. They want to ensure Claude uses Tailwind CSS for all styling. What is the best way to enforce this across the entire project?

* A) Add Use Tailwind CSS to every individual source file frontmatter.
* B) Use the Agent Skills feature to create a StylingAgent.
* C) Tell Claude Great job using Tailwind after every successful style change.
* **D) Include the requirement in the root CLAUDE.md file under a Styling Rules section.**

**Answer: D**
**Explanation:** Architectural consistency is managed through ambient context. For project-wide constraints like styling libraries state management or API patterns the CLAUDE.md file is the most efficient mechanism. By defining these rules once at the project root you ensure that every time Claude Code reads a file or proposes a change it aligns its suggestions with your technical stack.


---

## Question 35
**Question:** You are building a research agent that uses an MCP server to access a large database. The model frequently fails to use the correct SQL syntax for the specific database type. What is the most durable fix?

* A) Use a PostToolUse hook to fix the SQL before it runs.
* **B) Update the tool JSON schema description to include a SQL Cheat Sheet for the specific database.**
* C) Switch to a model with a larger context window.
* D) Tell the agent to be careful in its system prompt.

**Answer: B**
**Explanation:** Tool descriptions and JSON schemas are the primary evaluation mechanisms for agentic tool use under the Model Context Protocol. When an agent struggles with dialect-specific rules embedding technical constraints formatting instructions or mini cheat sheets directly into the tool description guarantees that this exact context is pulled into the model immediate reasoning loop at the precise moment of tool selection. This structural approach is significantly more durable than a general system prompt instruction which can degrade over long conversations.


---

## Question 36
**Question:** You want to use the Glob tool to find all JavaScript files in a repository but only those within the src directory. What is the most efficient pattern to use?

* A) src/*.js
* B) ls -R | grep .js
* **C) src/**/*.js**
* D) **/*.js

**Answer: C**
**Explanation:** Precision in tool calls is a hallmark of an expert agent. When navigating large repositories using generic patterns like **/*.js can cause the tool to scan thousands of irrelevant files like node_modules or build artifacts consuming extra time and potentially hitting file limits. By explicitly scoping the glob pattern to the src directory the search space is minimized. The pattern src/*.js only finds files directly inside the root of src and misses nested subdirectories.


---

## Question 37
**Question:** You are configuring Claude Code for a large monorepo. You want to prevent Claude from ever reading or indexing the .env.production file for security reasons. Which file should you use?

* A) .gitignore
* B) CLAUDE.md
* **C) .claudeignore**
* D) package.json

**Answer: C**
**Explanation:** The .claudeignore file is explicitly designed to exclude files and directories from Claude Code index and visibility ensuring sensitive credentials and production environment configurations remain completely local. While Claude Code respects standard .gitignore rules a dedicated .claudeignore file is the safest most definitive method to isolate sensitive assets from the AI active context window.


---

## Question 38
**Question:** A engineer is using Claude Code to navigate an unfamiliar codebase. They want to understand the high-level architecture before diving into specific files. Which workflow is most effective?

* A) Ask Claude to guess the architecture based on the file names.
* B) Instruct Claude to read every file in the root directory one by one.
* **C) Use the ls -R command followed by reading the README.md and CLAUDE.md files.**
* D) Run a grep search for the word Architecture.

**Answer: C**
**Explanation:** Effective codebase navigation with an AI agent follows the map-before-terrain principle. Brute-force reading or running intensive grep operations over a brand new project induces massive context window bloat and degrades reasoning efficiency. The optimal workflow relies on tiered exploration: build an immediate mental map using directory structure commands like ls -R then target and read high-density information stores specifically standard documentation files like README.md and tool-specific configuration profiles like CLAUDE.md.


---

## Question 39
**Question:** In a multi-agent system you want to use a Reviewer agent to check the work of a Researcher agent. To ensure the Reviewer is unbiased what context should the Coordinator provide to it?

* A) A summary of the Researcher confidence score.
* **B) Only the final research artifact produced by the Researcher.**
* C) The Researcher entire chain-of-thought and internal logs.
* D) The Researcher system prompt and tools.

**Answer: B**
**Explanation:** To achieve objective verification in multi-agent systems you must design for blind reviews. Providing the Researcher chain-of-thought or internal logs to the Reviewer can lead to reasoning sycophancy where the Reviewer agrees with the Researcher logic simply because it looks plausible or confident. The artifact isolation pattern ensures the Reviewer only sees the final result evaluating the outcome in isolation from the process.


---

## Question 40
**Question:** You are designing a Research Coordinator agent that needs to gather information on a new technology. It delegates to a Search subagent and an Analyst subagent. To minimize the total time to completion how should the Coordinator initiate these tasks?

* A) Call the Search agent wait for it to finish then call the Analyst agent.
* B) Use the Message Batches API for both subagents.
* C) Instruct the Analyst subagent to wait until the Search subagent finishes.
* **D) Emit multiple Task tool calls in a single response turn.**

**Answer: D**
**Explanation:** Optimizing agentic workflows for time-to-completion involves maximizing parallel execution. In complex missions where subtasks are independent the Coordinator should be designed to emit multiple tool calls in a single response turn. This allows the underlying infrastructure to spawn several subagents simultaneously significantly reducing the total wall-clock time compared to sequential one-by-one delegation.


---

## Question 41
**Question:** When designing a JSON schema for Structured Output you want to ensure the model extracts dates in the ISO 8601 format YYYY-MM-DD. What is the most effective way to enforce this?

* A) Pass a few-shot example showing a date in the correct format.
* **B) Set the data type to string and define a strict regex validation pattern using the pattern keyword inside the JSON schema parameters.**
* C) Allow the model to output any text string and clean it up using a python script later.
* D) Rely entirely on a system prompt instruction like: Always use YYYY-MM-DD format.

**Answer: B**
**Explanation:** While system prompts and few-shot examples strongly guide a model behavior they operate probabilistically and can occasionally fail under edge-case inputs. The most effective and deterministic approach to enforce syntactic formats in structured data extraction is to define programmatic constraints directly within the schema definition. By adding the pattern keyword with a regex constraint inside the JSON schema parameters you force the model generation tokens to comply with the schema format natively during decoding.


---

## Question 42
**Question:** You are building a custom MCP server to help engineers interact with a legacy bug tracking system. To ensure Claude selects the correct tool between search_bugs and get_bug_details what is the most important factor to optimize?

* A) The JSON Schema type of the parameters.
* **B) The detailed description field for each tool in the MCP server config.**
* C) The number of few-shot examples in the system prompt.
* D) The temperature setting of the model.

**Answer: B**
**Explanation:** Tool selection in the Model Context Protocol is driven by semantic matching between the user intent and the tool metadata. If two tools are semantically similar the description field is the only way for the model to distinguish between them. High-fidelity MCP tools should include usage boundaries in their descriptions specifically mentioning what the tool does and what it does not do. This provides a clear switching signal to the model reducing the risk of selection ambiguity.


---

## Question 43
**Question:** You are extracting structured information from messy unstructured medical records. Some fields like middle_name are often missing. How should you design your JSON schema to prevent the model from hallucinating values for these fields?

* A) Make every field required and instruct the model to use N/A if unknown.
* B) Build a Validation-Retry loop that fails if any field is empty.
* C) Use a larger model to ensure the model is smart enough to know when a field is missing.
* **D) Set nullable: true for optional fields and instruct the model to return null for missing data.**

**Answer: D**
**Explanation:** High-fidelity data extraction requires strict schema integrity. When an LLM is forced to populate a field marked as required in a JSON schema but the underlying data is completely missing from the source text it experiences structural pressure that frequently causes the model to hallucinate a plausible but completely fabricated value. The optimal architectural fix is explicit nullability. By explicitly defining nullable: true for optional properties and pairing it with a clear prompt instruction you provide a clean structural escape hatch.


---

## Question 44
**Question:** You are integrating Claude Code into a CI/CD pipeline to provide automated code reviews on every Pull Request. Which flag should you use to ensure the tool focuses only on the changes within the current project context?

* A) The --cloudeignore flag
* B) The --no-history flag
* **C) The -p or --project flag**
* D) The --output-format json flag

**Answer: C**
**Explanation:** Integrating agentic tools into CI/CD pipelines requires context isolation. In a monorepo or a shared runner environment the tool must be explicitly scoped to the project being reviewed. The -p or --project flag is the primary architectural lever for this. It ensures that Claude Code file discovery indexing and tool execution are restricted to the specified directory preventing context leakage where the AI reads files from unrelated projects.


---

## Question 45
**Question:** In an automated CI/CD environment you want to ensure that Claude Code session is completely isolated from any previous runs. What is the most reliable way to achieve this?

* A) Instruct Claude to start fresh in the system prompt.
* **B) Run Claude Code inside an ephemeral Docker container for each job.**
* C) Use the --no-history flag.
* D) Use the /clear command at the start of every script.

**Answer: B**
**Explanation:** Isolation is the cornerstone of secure and deterministic CI/CD pipelines. When using AI agents that have the power to write files and execute shell commands session pollution is a significant risk. The standard architectural solution is environment ephemerality spinning up a fresh isolated Docker container for every single CI run. This ensures that the agent always starts from a known good baseline with zero residual history file modifications or uncleared ambient tokens.


---

## Question 46
**Question:** You are running Claude Code in a CI environment with strict time limits of 10 minutes per job. How can you most effectively ensure the review completes within this window?

* A) Switch to a larger model to get the answer faster in fewer turns.
* **B) Use the --max-turns flag to limit the total number of steps Claude can take during the automated session.**
* C) Disable all Bash and Read tools to speed up the turns.
* D) Instruct Claude to work as fast as possible in the CLAUDE.md file.

**Answer: B**
**Explanation:** Running agentic tools in ephemeral CI environments requires deterministic boundaries. Unlike a local terminal where a human can wait a CI job has a fixed cost and a hard timeout. The --max-turns flag provides a hard boundary on the conversation length preventing agentic loops where the AI gets stuck trying to fix a complex problem over dozens of turns from consuming the entire CI budget or causing an ungraceful timeout.


---

## Question 47
**Question:** You want to build a research system that can process 500 different documents simultaneously to extract key trends. Which combination of features is most appropriate for this high-volume non-real-time task?

* **A) Message Batches API with specialized subagents for document segments.**
* B) Claude Code in bulk mode.
* C) Prompt Caching for all 500 documents in a single context window.
* D) Standard Messages API with 500 parallel threads.

**Answer: A**
**Explanation:** For massive asynchronous workloads like bulk document analysis that do not require instant real-time responses the Message Batches API is the optimal architectural choice. It provides a significant 50% discount on token costs and bypasses typical real-time rate limits by processing requests asynchronously within a 24-hour window. Combining the Batch API with a multi-agent decomposition strategy where specialized subagents independently handle individual document segments enables a highly scalable divide-and-conquer architecture.


---

## Question 48
**Question:** A pharmaceutical company is extracting dosage information from 5000 legacy PDF protocols. Some PDFs are low-quality scans. Which combination of features ensures the highest data quality?

* **A) Claude Sonnet with Vision and Validation-Retry Loop.**
* B) A smaller model with Prompt Caching.
* C) Message Batches API with Standard Messages API.
* D) A large model with 100 few-shot examples.

**Answer: A**
**Explanation:** High-stakes extraction from dirty data low-quality scans requires a multi-modal defensive architecture. Relying solely on text-based OCR is insufficient because OCR transcription errors will be propagated directly into the model context window. By using Claude Vision the model can analyze the raw pixels of the document directly resolving visual ambiguities that standard text OCR might misinterpret. Pairing this with a Validation-Retry Loop where an external validation script programmatically checks the output for format errors and automatically requests a correction provides the highest possible precision.


---

## Question 49
**Question:** A support agent is being used for troubleshooting complex hardware issues. The interaction often spans 30+ turns. After 20 turns the agent starts repeating the same basic diagnostic steps. What is the most likely cause?

* A) The model has run out of tokens in its context window.
* B) The temperature is set too high.
* **C) The model attention is being diluted by the growing conversation history causing it to lose track of completed steps.**
* D) The user is providing inconsistent information.

**Answer: C**
**Explanation:** Looping behavior and repetition are standard technical symptoms of context saturation. As a conversation grows over many turns the model attention mechanism must distribute its focus over an increasing volume of tokens making it progressively more difficult to accurately distinguish between completed steps and next steps. Architects should implement context maintenance strategies such as using an external state tool to track diagnostic progress or performing periodic context pruning.


---

## Question 50
**Question:** To achieve a target of 80% first-contact resolution a support agent must manage complex multi-turn interactions without losing track of the user original issue. Which architectural pattern is most effective for maintaining focus in long sessions?

* A) Switch to a smaller model to minimize the cost of long-running sessions.
* **B) Use the Write tool to maintain a CASE_SUMMARY.md scratchpad file that is read at the start of every turn.**
* C) Instruct the agent to be brief and resolve the issue quickly in the system prompt.
* D) Raise the context window to 200000 tokens for every turn.

**Answer: B**
**Explanation:** Effective state management is critical for agents performing complex multi-turn resolutions. While Claude has a massive context window relying solely on conversational history memory can lead to attention dilution as the session grows. The scratchpad pattern involves giving the agent a tool to write to a persistent state file like CASE_SUMMARY.md which acts as its short-term working memory. By reading this file at the start of every turn the agent maintains a high-fidelity summary of the core goals facts gathered and steps remaining.


---

## Question 51
**Question:** An architect is designing an extraction system for Legal Contracts. They want to ensure that if a specific clause is Ambiguous the model flags it for human review. How should the tool be designed?

* A) Set the temperature to 0.7 so the model provides multiple guesses for ambiguous clauses.
* B) Tell the model to try its best and never skip a field.
* C) Use a PostToolUse hook to check if the extracted text contains the word maybe.
* **D) Add a field is_ambiguous to the JSON schema and instruct the model to set it to true if uncertain.**

**Answer: D**
**Explanation:** Safe agentic design follows the escalation principle. In high-fidelity tasks like legal extraction forcing a model to provide a binary answer to an ambiguous input is a hallucination trap. The architectural solution is to normalize uncertainty directly within the data structure. By providing a dedicated uncertainty channel such as an is_ambiguous boolean field you give the agent a structural safety valve. This allows the system to autonomously identify high-risk extractions and route them via a human-in-the-loop pattern to an expert preserving the efficiency of automation without compromising critical accuracy.


---

## Question 52
**Question:** A team is seeing a high number of false positive style warnings in their automated PR reviews from Claude Code. Which strategy is most effective for minimizing these false positives?

* A) Switch to a smaller model for the reviews.
* B) Raise the temperature to 0.7 to make the model more lenient.
* C) Disable the Bash tool to prevent the agent from running linters.
* **D) Add explicit Negative Constraints to a specialized CLAUDE.md file such as Do not flag missing semicolons.**

**Answer: D**
**Explanation:** Tuning the review threshold in automated AI agents is a core architectural task. In a CI/CD environment noise or false positives can lead to alert fatigue and cause engineers to ignore AI feedback. The most effective way to tune this sensitivity is through negative constraints and project style grounding in the CLAUDE.md file. By explicitly defining what the AI should not care about you restrict its reasoning space to high-value findings.


---

## Question 53
**Question:** An agent needs to use the customer_identity tool to verify a user before accessing private data. In testing the agent occasionally tries to call get_account_details without first calling verify_identity. What is the most effective fix?

* A) Add a negative constraint: NEVER call details before verification.
* **B) Build a Prerequisite Gate in the backend that returns an error if get_account_details is called without a valid session token.**
* C) Make the verify_identity tool description longer and more urgent.
* D) Use tool_choice set to any for the first turn.

**Answer: B**
**Explanation:** When designing secure agentic systems you must design for tool dependencies. Relying solely on soft prompt-based instructions or negative constraints is fundamentally probabilistic. The most robust architectural solution is programmatic enforcement at the API or service layer. By requiring a valid verification or session token as a mandatory parameter for sensitive tools and only granting that token via a successful verify_identity execution you establish a hard technical dependency. If the agent attempts to skip the step the backend safely blocks the operation and surfaces a structured error message forcing the agent to self-correct predictably.


---

## Question 54
**Question:** You want to ensure that Claude Code never runs npm publish or any other deployment command during an interactive session. Which implementation is the most robust?

* A) Only run Claude Code in a read-only Docker container.
* B) Tell the engineer to watch the terminal carefully.
* C) Add a DANGER warning to the CLAUDE.md file.
* **D) Build a PreToolUse hook that exits with code 2 if a deployment command is detected.**

**Answer: D**
**Explanation:** Safety and risk mitigation in autonomous agent workflows require programmatic enforcement. While instructions in CLAUDE.md or system prompts are important for guidance they remain entirely probabilistic and can still be bypassed or forgotten by the model during complex deep-context reasoning tasks. Implementing a deterministic PreToolUse Hook establishes a non-negotiable security boundary. The hook intercepts and parses the raw shell command strings before they are ever dispatched to the underlying system shell. If a forbidden pattern like npm publish is detected the hook immediately blocks execution and exits with an error status code.


---

## Question 55
**Question:** A multi-agent research system uses a Manager to coordinate 10 subagents. You notice the Manager frequently gets confused and re-assigns the same sub-task multiple times. Which architectural fix is most effective?

* A) Raise the temperature of the Manager.
* B) Add more subagents to reduce the Manager cognitive load.
* **C) Instruct the Manager to maintain a Task Board file and read it at the start of every turn.**
* D) Use a smaller model for the Manager to save on token costs.

**Answer: C**
**Explanation:** Coordinating multiple parallel subagents is an information-dense task that can quickly saturate an orchestrator context window. To prevent reasoning drift and redundant task assignments the Manager agent requires a persistent source of truth rather than relying solely on passing conversation history. Implementing the Task Board Pattern allows the orchestrator to interactively update a structured file that acts as a physical state machine. By forcing the Manager to inspect this file at the beginning of each turn you provide a clear static state map that acts as programmatic memory.


---

## Question 56
**Question:** A customer support agent is receiving a high volume of off-topic requests such as asking for weather updates. Which architectural component most efficiently prevents the main support agent from wasting tokens on these requests?

* **A) Build a lightweight Routing Classifier using a smaller model to filter or redirect requests before they reach the main agent.**
* B) Raise the max_tokens to allow the agent to explain why it cannot help.
* C) Add a No Off-Topic section to the system prompt.
* D) Set the temperature to 0.0 to ensure the agent stays focused.

**Answer: A**
**Explanation:** Token efficiency is a major architectural concern in production support systems. Processing every user message with a high-capability model is expensive especially when many messages are trivial or irrelevant. A tiered triage architecture uses a lightweight Routing Classifier to analyze the intent of the incoming message first. If the message is off-topic the classifier can trigger a hard-coded rejection response or redirect the user bypassing the expensive main agent entirely.


---

## Question 57
**Question:** A support agent for an airline must handle flight changes. If a user becomes frustrated or uses abusive language the agent should immediately hand over to a human supervisor. How can this Sentimental Escalation be implemented most reliably?

* A) Raise the model temperature to 0.9 to make it more empathetic.
* **B) Build an MCP tool named escalate_to_human and a PostToolUse hook that analyzes the agent output sentiment.**
* C) Tell the user to calm down if they get angry.
* D) Instruct the agent to be polite in the system prompt.

**Answer: B**
**Explanation:** Reliable human handover is a core guardrail requirement for enterprise-grade autonomous customer support. A single system prompt instruction is insufficient because a highly frustrated customer might trap the model in a loop of unhelpful apologetic text. The most robust architectural pattern is a dual-trigger escalation strategy: provide the agent with an explicit tool and clear instructions on when to invoke it while implementing an asynchronous external validation hook that checks the conversation raw text for prohibited sentiment patterns. If the hook triggers it programmatically overrides the LLM session and forwards the interaction to a human agent.


---

## Question 58
**Question:** To programmatically parse the results of an automated Claude Code security scan in a GitHub Action which CLI option provides the most reliable data format?

* A) The --format markdown option
* **B) The --output-format json option**
* C) The --export log option
* D) The --quiet option

**Answer: B**
**Explanation:** Automated security gates and CI/CD quality gates must be programmatically actionable. While Markdown or raw text formats are ideal for human consumption they are brittle and prone to parsing errors when handled by automation scripts. The --output-format json flag structures Claude reasoning discoveries and metadata into a standardized machine-readable format allowing CI/CD workflows to seamlessly parse the payload and automatically trigger conditional build failures.


---

## Question 59
**Question:** You are building a CI/CD pipeline that uses Claude Code to automatically update documentation. To prevent the agent from accidentally deleting the SUMMARY.md file what is the best safeguard?

* A) Use a smaller model that is less capable of complex deletes.
* B) Set the file permission to Read Only in the CI environment.
* C) Add a warning in the CLAUDE.md file: DO NOT DELETE SUMMARY.md.
* **D) Build a PreToolUse hook that blocks any rm command targeting that specific file.**

**Answer: D**
**Explanation:** In automated workflows safety boundaries must be treated as strict programmatic constraints. While instructions inside a CLAUDE.md file provide baseline policy direction model execution remains probabilistic. Setting file systems to read-only stops the deletion by throwing a system error but forces an ungraceful breaking failure mid-execution. A PreToolUse Hook acts as a deterministic programmatic interceptor that evaluates the exact tool parameters before they are sent to the shell providing a 100% reliable guarantee that the targeted resource is safe.


---

## Question 60
**Question:** When extracting data from a multi-column table in a PDF you receive a stop_reason of max_tokens and the JSON is cut off. What is the best immediate fix?

* **A) Raise the max_tokens value in the API request to accommodate the full expected size of the JSON output.**
* B) Provide few-shot examples of smaller tables.
* C) Enable Extended Thinking mode.
* D) Switch to tool_choice type any.

**Answer: A**
**Explanation:** A max_tokens stop reason is a physical resource boundary signal indicating that the model response reached the output token budget set in your API request before it could finish generating the full payload. For structured data extraction tasks which often involve verbose JSON formatting you must ensure the max_tokens parameter is set high enough to accommodate the worst-case output length.


---
