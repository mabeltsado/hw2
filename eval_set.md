# Evaluation Set

### Evaluation Goal:
Assess the model’s ability to synthesize user research into clear, actionable, and non-hallucinated insights suitable for leadership audiences.

---

## Case 1: Normal Case (Clear Patterns)

### Input:
Users consistently mentioned frustration with not understanding their energy bill. Many said charges felt unpredictable and confusing. Several participants said they would prefer a simple monthly breakdown showing exactly what they are paying for. A few users mentioned calling customer support but still leaving confused.

### What a good output should do:
- Identify a clear insight about lack of transparency
- Summarize the core user frustration
- Translate into an actionable opportunity
- Avoid repeating raw notes

---

## Case 2: Edge Case (Messy + Unstructured Notes)

### Input:
billing confusing, not sure why costs change  
one user said "feels random"  
another liked app but still confused about charges  
some said support helps but takes too long  
trust issue? maybe transparency problem  

### What a good output should do:
- Cleanly synthesize fragmented thoughts
- Identify a central theme (confusion + trust)
- Avoid just re-listing notes
- Produce structured, readable insights

---

## Case 3: Failure-Prone Case (Conflicting Feedback)

### Input:
Some users said they love the flexibility of variable pricing and feel it saves them money. Others said the same variability makes it hard to predict bills and causes frustration. A few users said they don’t mind variability as long as they understand it better.

### What a good output should do:
- Acknowledge conflicting perspectives
- Avoid choosing one side as “truth”
- Synthesize nuance into a balanced insight
- Suggest a thoughtful opportunity (e.g., education vs simplification)

---

## Case 4: Risk Case (Hallucination Risk)

### Input:
Users mentioned wanting better tools. Some said current features are not enough.

### What a good output should do:
- Avoid inventing specific tools or features
- Clearly state that feedback is vague
- Still attempt a high-level insight
- Flag need for more research or clarification

---

## Case 5: Strategic Case (High-level/Leadership-Level Output)

### Input:
Across interviews, users expressed a desire for more control over their energy usage. Many said they would change behavior if they had better visibility into usage patterns. Several users mentioned wanting proactive recommendations rather than reacting after receiving a high bill.

### What a good output should do:
- Elevate insight to a strategic level
- Connect behavior + motivation
- Translate into actionable opportunity
- Sound appropriate for leadership (not overly tactical)