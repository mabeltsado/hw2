# HW2 Report: AI-Assisted User Research Synthesis

---

Business Use Case

Teams that run user research often hit a bottleneck after data collection. While interviews, surveys, and usability testing generate valuable insights, turning those raw notes into something clear and actionable for leadership takes time. Researchers end up spending hours organizing and formatting findings before they can even begin sharing them, which can slow down decision-making.

This prototype focuses on speeding up that synthesis step. The idea is simple: a researcher pastes in raw research notes, and the system generates a structured summary with key themes, pain points, recommendations, and a confidence check. In this case, the workflow is grounded in energy sector research, where billing transparency consistently came up as a major issue. The value here is reducing time spent on formatting, improving consistency across outputs, and helping teams get insights in front of stakeholders faster.

Model Choice

The final model used was claude-haiku-4-5-20251001.

I initially tried a few other models, including claude-3-5-haiku, claude-3-5-sonnet, and claude-3-haiku, but they were not available under my API access and returned errors. Because of that, I selected the Haiku 4.5 model, which was both accessible and fast.

Baseline vs. Final Prompt Design:

The biggest improvement in this project came from refining the prompt. The baseline approach was very simple. I passed the notes with a general instruction like:
“Please summarize the following user research notes.” The output technically worked, but it wasn’t very useful. It mostly restated the input in paragraph form and didn’t clearly separate insights, pain points, or recommendations. It felt more like a cleaned-up version of the notes rather than something ready for leadership.

The final prompt was much more structured. I explicitly defined the role of the model and the format of the output, asking for sections like Key Themes, Core User Pain Points, Actionable Recommendations, and Confidence & Caveats. This made a big difference. The outputs became more organized, more strategic, and more actionable. Instead of just summarizing what users said, the model started identifying patterns and translating them into recommendations. The addition of a confidence section also helped make the output feel more honest and grounded, especially when the input was limited. Overall, the improvement came from shifting the task from “summarize” to “synthesize for a leadership audience.”

Where the Prototype Still Fails:

Even with the improved prompt, there are still clear limitations. The model struggles most when the input is vague or incomplete. For example, if the notes just say something like “users want better tools,” the model tends to fill in the gaps with assumptions, which can lead to recommendations that aren’t actually supported by the data.

It also doesn’t fully handle conflicting feedback. When users have different opinions, the model sometimes smooths over that tension instead of clearly acknowledging it. On top of that, it can overinterpret emotional language and make issues seem more widespread or severe than they actually are. Because of this, the output cannot be treated as final. It still requires human judgment, especially to validate that insights are accurate and appropriately scoped.

Deployment Recommendation:

I would recommend using this workflow, but only with clear guardrails in place. The biggest requirement is a human review step. A researcher should always check the output before it is shared with leadership, since the model cannot verify whether its conclusions are fully supported by the data.It would also help to set expectations around input quality. The system performs much better when it has detailed notes with clear examples or quotes. Without that, the risk of vague or misleading output increases.

Finally, teams should be transparent that this is an AI-assisted tool. It works best as a way to speed up the first draft, not replace the researcher’s role in interpreting and communicating insights. Used this way, the tool can be genuinely valuable. It reduces time spent on structuring outputs and helps researchers focus more on analysis and decision-making, while still keeping humans in the loop where it matters most.
