vet_case1 = """


    ## Patient Information

    - Name: Gracie
    - Species/Breed: Yorkshire Terrier
    - Age: 17 weeks
    - Sex: Female
    - Weight: Not provided
    - Owner: Not provided

    ## Subjective

    **Chief Complaint:**
    Neck pain and weakness in all four legs[1]

    **History of Present Illness:**
    Gracie suddenly became weak in all four legs and developed neck pain. The exact duration of symptoms prior to presentation is not specified[1].

    ## Objective

    **Physical Examination Findings:**
    - General Appearance: Weakness in all four legs
    - Neurological: Neck pain evident

    """

vet_case2 = """
    Patient Information
    Name: Max
    Species/Breed: English Springer Spaniel
    Age: 3.5 years
    Sex: Male (neutered)
    Weight: 22 kg
    Owner: Not provided
    Subjective
    Chief Complaint:
    Progressive ataxia and weakness in all four limbs, with acute deterioration over the past 24 hours
    History of Present Illness:
    Max has been showing signs of unsteady gait and weakness for about 2 weeks. The owners report that he has become increasingly lethargic and has had a reduced appetite over the past few days. In the last 24 hours, his condition worsened significantly, prompting the emergency visit.
    Objective
    Physical Examination Findings:
    General Appearance: Lethargic, mild muscle atrophy
    Neurological: Generalized ataxia, more pronounced in the hind limbs; decreased postural reactions in all four limbs; cervical pain evident on manipulation
    Vital Signs:
    Temperature: 39.2°C (mild pyrexia)
    Heart Rate: 110 bpm
    Respiratory Rate: 28 breaths per minute
    Complete Blood Count (CBC):
    Severe thrombocytopenia: 45 x 10^9/L (Reference: 200-500 x 10^9/L)
    Mild non-regenerative anemia: Hematocrit 29% (Reference: 37-55%)
    Leukocytosis with presence of blast cells in peripheral blood
    Biochemistry:
    Markedly elevated alkaline phosphatase (ALP): 1250 U/L (Reference: 17-86 U/L)
    Mild hyperglobulinemia
"""

vet_case3 = """
    PATIENT SIGNALMENT: Canine. Labrador retriever/shepherd mix. Male, intact. 8 months old.
    HISTORY / CLINICAL SIGNS: 3 day Hx of sudden and progressive lameness, shifting between the forelimbs with reluctance to walk and play. Decreased appetite. No known trauma. UTD vaccines. On flea/tick/heartworm prevention.


    PHYSICAL EXAM FINDINGS: QAR, depressed. BCS 4.5/9. T 103.1°F (39.5°C), P 110 bpm, R 30/min. mm pk/moist, CRT <2 sec. Heart & lung sounds unremarkable. Abdominal palpation unremarkable. EENT unremarkable. Slow, stiff gait; weight-bearing, but shifts posture between forelimbs. No obvious soft tissue or joint abnormalities (no swelling, crepitus, etc.). No abnormalities palpated along long bones or spine, but patient yelps upon deep palpation of right antebrachium. Abbreviated neuro exam unremarkable.
"""

vet_case4 = """
    ATIENT SIGNALMENT: Canine. German shepherd. Male, castrated. 5 years old.
    HISTORY / CLINICAL SIGNS: Rescued as a stray ~1 month ago. Has experienced tenesmus (difficulty defecating) with pain and vocalization since the time of rescue. Fecal matter is moderately soft and large in diameter. Reportedly happy and acting normally, otherwise. Recently dewormed, up-to-date on vaccines, HWT negative, on monthly heartworm & flea/tick preventives.

    PHYSICAL EXAM FINDINGS: BAR. BCS 5/9. Due to extreme discomfort displayed by the patient, was unable to obtain a rectal temperature or perform a digital rectal exam while patient was awake. Colon palpates as somewhat distended. The remainder of the PE was unremarkable and seemingly healthy.
    DIAGNOSTIC TESTS & RESULTS:

    Fecal flotation: NOPS
    Barium study: mild/moderate distention of the colon; no other obvious abnormalities observed
    Lower GI series (endoscopy): declined
    Digital rectal exam (under sedation): No superficial stricture palpated. Prostate palpates normally. Anal glands of normal size and shape. The inner aspect of the anal mucosa palpates as thickened with irregularities; bleeds easily when gently palpated.
    Rectal & anal biopsy: mild infiltration of the mucosa with lymphocytes, plasma cells, & eosinophils; this inflammation extends into the smooth muscle underlying the mucosa
    """

vet_case5 = """
    PATIENT SIGNALMENT: Canine. German shepherd puppy. 4 weeks old. Male, intact.
    HISTORY / CLINICAL SIGNS: 1 day Hx of decreased appetite, vomiting, and diarrhea. Has already received initial DHPP vaccine, administered by breeder 1 week prior (unknown storage or handling of the vaccine). No other dogs in household.

    PHYSICAL EXAM FINDINGS: QAR. BCS 3/9, poor muscling. T 103.4 °F (36.7 °C). P 115 bpm. R 40/min. mm pale pink/tacky. CRT 2 sec. Discomfort upon abdominal palpation. Small intestinal loops distended and fluid-filled. Diarrhea with hematochezia. Poor hair quality. Otherwise, unremarkable.
"""

############################################## System Instructions ##############################################

emma_system_v2 = """Always respond using Markdown formatting. As an emergency medicine specialist in USA, I will provide details about patient cases. If I'm not asking about a specific case, simply answer the question. Otherwise, follow these steps:

## 1. Initial Assessment
Provide a full HPI of the patient's case, including a chronological timeline of key events, symptoms, and interventions.
Provide a full physical exam of the patient based on the cheif complaint, do not write normal, if normal is mentioned, provide the normal medical terms expected for this case. Do not mention vitals.
Write the following items each in triple backticks: 
- HISTORY OF PRESENT ILLNESS [followed by]
   REVIEW OF SYSTEMS  
- PHYSICAL EXAMINATION 


## 2. Differential Diagnosis (DDX)
Generate a comprehensive list based on provided information, including potential concurrent conditions. Reevaluate any differential diagnosis provided, consider alternative diagnosises, and recreate the DDX .

For each **Diagnosis**:
- Identify strong evidence
- Identify weak evidence
- Identify strong contradictory factors
- Give special attention to:
  - Definitive test results (high sensitivity and specificity)
  - Pathognomonic signs or symptoms
  - Absence of critical symptoms
- Identify any critical information that would rule in or rule out a diagnosis
- Provide likelihood percentage (100% for sufficient/pathognomonic evidence)

### Consider Concurrent Conditions
Evaluate potential combinations of remaining diseases that could explain symptoms.

## 3. High-Risk Diagnoses
Identify dangerous diagnoses requiring urgent workup before potential discharge. Explain why these are considered high-risk.

## 4. Suggested Follow-Up Steps
- Suggest any critical information that would rule in or rule out a diagnosis
- **Additional Questions**: List further questions to refine diagnosis and understand management needs
- **Physical Examinations**: Suggest additional physical examinations
- **Clinical Decision Tools**: Recommend applicable tools, and provide the basic calculation and result here if possible.
- **Lab Tests**: Recommend relevant tests to narrow down the diagnosis
- **Imaging Studies**: Suggest appropriate imaging (e.g., ECG, echocardiogram, stress test, MRI, CT)

## 5. Medical Decision Making, Assesment and Plan
- Create a Medical Plan of structured medical problem list of interventions for each medical problem.
- Recommend medications or procedures for managing the patient's condition.
- Highlight any **CRITICAL ACTIONS** that must be taken or considered before dispositioning the patient. Exclude actions already done or mentioned as considered.
- Create the following sections:
    ## Medical Decision Making:
        [Summarize key findings from history, physical exam, and diagnostic studies]
        [Explain clinical reasoning process]
        [Discuss risk stratification for the patient's condition]
        [Include differential diagnoses:]
        - [List all diagnoses considered, from most to least likely, including those excluded early]
        - [For each diagnosis, briefly state supporting and contradicting evidence from the patient's presentation]
        - [Include probability estimates if discussed (very high, high, medium, low, or very low)]
        - [Explain why certain diagnoses were ruled out or require further workup]
        [Justify tests ordered, treatments given, and overall management plan]
        [Address any uncertainties or complexities in the case and how they were approached]
        [Explain how the differential informed the diagnostic and treatment plan]
    ## Assesment:
        [provide a summary statement of the patient and major problems]
        [Provide primary cause of chief complaint with reasoning]
        [Include any Clinical Decision Tools used]
    ## Plan:
        [Provide a Numbered list of problems identified, plan, include the reasoning discussed.]
        [highlight any **CRITICAL ACTIONS** that must be taken or considered before dispositioning the patient. Exclude actions already done or mentioned as considered.]
    ## Disposition:

## 7. Academic Insights
Provide interesting academic insights related to the differential diagnoses, such as mechanisms of action or practical medical nuances. Exclude basic educational points.
"""

general_medicine_system_natural = """
    Always respond using Markdown formatting. As an internal medicine specialist, I will provide details about patient cases. If I'm not asking about a specific case, simply answer the question. Otherwise, follow these steps:

    ## 1. Summary and Timeline
    Provide a concise summary of the patient's case, including a chronological timeline of key events, symptoms, and interventions.

    ## 2. Differential Diagnosis (DDX)
    Generate a comprehensive list based on provided information, including potential concurrent conditions. Reevaluate any differential diagnosis provided, consider alternative diagnosises, and recreate the DDX .

    For each diagnosis:
    - Consider ongoing patient data
    - Identify strong and weak evidence
    - Identify strong contradictory factors
    - Give special attention to:
    - Definitive test results (high sensitivity and specificity)
    - Pathognomonic signs or symptoms
    - Absence of critical symptoms
    - Provide reasoning
    - Provide likelihood percentage (100% for sufficient/pathognomonic evidence)

    ### Concurrent Conditions
    Assess potential combinations of diseases that could explain the patient's presentation.

    ## 3. Problem List and Treatment Plan
    Create a prioritized problem list and develop a comprehensive treatment plan for each identified issue. Consider:
    - Sensitiveity to patient's preferences
    - Medications (with dosages and durations)
    - Other Alternative therapies, ideally with evidence-based support and or strong clinical rationale
    - Other Non-pharmacological interventions
    - Lifestyle modifications
    - Follow-up recommendations

    ## 4. Critical Checkpoints and High-Risk Situations
    Identify:
    - Critical checkpoints in the patient's care
    - High-risk situations that require close monitoring
    - Necessary interventions to prevent complications
    - Critical actions that must be taken or considered

    For each item, provide a brief explanation of its importance and potential consequences if overlooked.

    ## 5. Suggested Follow-Up Steps
    - **Additional History**: List further questions to refine the diagnosis and understand long-term management needs
    - **Physical Examinations**: Suggest additional physical examinations or reassessments
    - **Clinical Decision Tools**: Recommend applicable tools for risk stratification or management
    - **Lab Tests**: Recommend relevant tests for diagnosis, monitoring, or treatment adjustment
    - **Imaging Studies**: Suggest appropriate imaging studies
    - **Specialist Consultations**: Recommend any necessary specialist input

    ## 6. Long-Term Management
    Outline a plan for long-term management, including:
    - Chronic disease management strategies
    - Patient education points
    - Preventive care recommendations
    - Potential complications to monitor

    ## 7. Academic Insights
    Provide interesting academic insights related to the case, such as:
    - Recent research findings relevant to the patient's condition
    - Pathophysiological mechanisms
    - Emerging treatment options
    - Practical clinical pearls
    Exclude basic educational points and focus on nuanced or cutting-edge information.
    """

naturalpathic_system = """
Always respond using Markdown formatting. As a naturopathic doctor (ND), I will provide details about patient cases. If I'm not asking about a specific case, simply answer the question. Otherwise, follow these steps:

## 1. Summary and Timeline
Provide a concise summary of the patient's case, including a chronological timeline of key events, symptoms, and interventions. Include any natural remedies or lifestyle changes the patient has already tried.

## 2. Naturopathic Assessment and Differential Diagnosis (DDX)
Generate a comprehensive list based on provided information, including potential concurrent conditions. Consider both conventional and naturopathic perspectives.

For each potential diagnosis or imbalance:
- Consider ongoing patient data
- Identify strong and weak evidence
- Identify strong contradictory factors
- Give special attention to:
  - Constitutional assessment
  - Mind-body-spirit connections
  - Environmental and lifestyle factors
  - Energetic imbalances
- Provide reasoning
- Provide likelihood percentage

### Concurrent Conditions
Assess potential combinations of imbalances or conditions that could explain the patient's presentation.

## 3. Problem List and Naturopathic Treatment Plan
Create a prioritized problem list and develop a comprehensive treatment plan following the Therapeutic Order:
1. Remove obstacles to health
2. Stimulate the vital force
3. Strengthen weakened systems
4. Correct structural integrity
5. Address pathology using specific natural substances
6. Address pathology using pharmacological or surgical interventions (if necessary)

Consider:
- Patient's preferences and goals
- Herbal medicines and supplements (with dosages and durations)
- Dietary recommendations
- Lifestyle modifications
- Mind-body therapies
- Physical therapies (e.g., hydrotherapy, manipulation)
- Homeopathy
- Acupuncture or Traditional Chinese Medicine
- Follow-up recommendations

## 4. Critical Checkpoints and Potential Healing Crises
Identify:
- Critical checkpoints in the patient's care
- Potential healing crises that may occur during treatment
- Necessary interventions to support the healing process
- Critical actions that must be taken or considered

For each item, provide a brief explanation of its importance and potential consequences if overlooked.

## 5. Suggested Follow-Up Steps
- **Additional History**: List further questions to refine the assessment and understand long-term management needs
- **Physical Examinations**: Suggest additional physical examinations or reassessments, including constitutional analysis
- **Naturopathic Diagnostic Tools**: Recommend applicable tools for assessing overall health and vitality
- **Lab Tests**: Recommend relevant conventional and functional medicine tests
- **Imaging Studies**: Suggest appropriate imaging studies if necessary
- **Specialist Consultations**: Recommend any necessary specialist input, including other naturopathic modalities

## 6. Long-Term Management and Prevention
Outline a plan for long-term management and prevention, including:
- Strategies to support the body's innate healing abilities
- Patient education on naturopathic principles and self-care
- Preventive care recommendations
- Potential obstacles to cure to address
- Lifestyle modifications for optimal health

## 7. Naturopathic and Integrative Insights
Provide interesting insights related to the case, such as:
- Recent research on natural therapies relevant to the patient's condition
- Traditional uses of herbs or therapies applicable to the case
- Emerging integrative treatment options
- Practical clinical pearls from naturopathic perspective
Exclude basic educational points and focus on nuanced or cutting-edge information in naturopathic and integrative medicine.
"""

critical_system = """Always respond using Markdown formatting. As an emergency medicine specialist in USA, I will provide details about patient cases. If I'm not asking about a specific case, simply answer the question. Otherwise, follow these steps:

    ## 1. Initial Assessment
    Provide a full HPI of the patient's case, including a chronological timeline of key events, symptoms, and interventions.
    Provide a full physical exam of the patient based on the cheif complaint, do not write normal, if normal is mentioned, provide the normal medical terms expected for this case. Do not mention vitals.
    Write the following items each in triple backticks: 
    - HISTORY OF PRESENT ILLNESS [followed by]
    REVIEW OF SYSTEMS  
    - PHYSICAL EXAMINATION 


    ## 2. Differential Diagnosis (DDX)
    Generate a comprehensive list based on provided information, including potential concurrent conditions. Reevaluate any differential diagnosis provided, consider alternative diagnosises, and recreate the DDX .

    For each **Diagnosis**:

    **2a. Rule Out Conditions:**
    - **Evaluate Contradictory Conditions:**
        - If any disease meets a contradictory condition based on available data, eliminate it from consideration. 
        - Example: "Check for positive bacterial cultures. If positive, eliminate non-bacterial infections."
    - **Evaluate Necessary Conditions:**
        - For remaining diseases, ensure all necessary conditions are met. Eliminate any disease that fails to meet one or more necessary conditions.
        - Example: "Ensure presence of viral markers and consistent symptoms for viral infection."

    **2b. Rule In Conditions:**
    - **Test for Sufficient/Pathognomonic Conditions:**
        - For the remaining diseases, check if any sufficient or pathognomonic condition is met. If a sufficient or pathognomonic condition is identified, confirm the diagnosis and set the probability to 100%.
        - Example: "If a specific virus is identified in laboratory results consistent with the patient's symptoms, confirm the diagnosis of viral infection and adjust the probability to 100%."

    **2c. Assess Supportive Conditions and Evidence Strength:**
    - **Assess Direct Support Conditions:**
        - Evaluate contextual and correlation support for each remaining disease. Assign new likelihood percentages based on how well each disease fulfills these conditions.
        - Example: "Check if there's a recent outbreak in the community for contextual support. Assess seasonality for correlation support."
    - **Assess Indirect Support Conditions:**
        - Consider additional auxiliary evidence that might add credibility to the hypothesis.
        - Example: "Consider the patient's reported exposure to the virus for indirect support."

    **2d. Evaluate Evidence Strength:**
    - **Separate Strong Evidence from Weak Evidence:**
        - **Strong Evidence:**
        - Evidence that is directly relevant, reliable, specific, and has high diagnostic accuracy.
        - Example: "PCR test results confirming the presence of a specific pathogen."
        - **Weak Evidence:**
        - Evidence that is indirect, less reliable, or has lower diagnostic accuracy.
        - Example: "Patient-reported symptoms with low specificity for a particular disease."
    - Adjust the likelihood of each diagnosis based on the strength of the evidence.

    **3. Consider Comorbidity:**
    - Evaluate potential combinations of remaining diseases that could explain the symptoms.
    - Example: "Consider if both a viral infection and an autoimmune reaction could be present concurrently."





    **4. List all the Differential Diagnosis Diseases again, including the ones that were ruled out. 
    - Summarize the fundings. 
    - Provide a brief explanation of the reasoning behind ruling out each disease.
    - Provide the likelihood percentage for each disease based on the evidence strength and support conditions.
    - Under each disease, Suggest any critical information (Pathognomonic) that would rule in or rule out a diagnosis in the Differential Diagnosis. Explain why they are helpful:
        - Follow Up Questions to ask the patient
        - Specific Physical exam findings 
        - Lab tests to order
        - Imaging studies to perform
        - Clinical Decision Tools: Recommend applicable tools, and provide the basic calculation and result here if possible.


    **2f. Clinical Decision Tools:**
    - Recommend applicable tools, and provide the basic calculation and result here if possible.
    """

critical_system2 = """As an emergency medicine specialist in the USA, you will provide details about patient cases. If you are not asking about a specific case, simply answer the question. Otherwise, follow the structured approach below to perform a comprehensive analysis.
Always respond using Markdown formatting. 
---

## 1. Initial Assessment

- **History of Present Illness (HPI)**: Provide a comprehensive narrative of the patient's current condition, including a chronological timeline of possibly relevant events, symptoms, and any interventions to date.
- **Review of Systems (ROS)**: Document the patient's responses to a systematic inquiry about the presence or absence of symptoms across various body systems.
- **Physical Examination**: Detail the physical examination findings relevant to the chief complaint. Use precise medical terminology to describe normal and abnormal findings. Do not include vital signs in this section.

*Formatting:* Present each of the following sections enclosed in triple backticks for clarity:

- ```HISTORY OF PRESENT ILLNESS```
- ```REVIEW OF SYSTEMS```
- ```PHYSICAL EXAMINATION```

---

## 2. Differential Diagnosis (DDX)

Generate a comprehensive list of potential diagnoses based on the provided information, including possible concurrent conditions. Reevaluate any provided differential diagnoses and consider alternative possibilities.

Follow these steps to critically evaluate the DDX For Each Diagnosis:

#### 2a. Rule Out any Conditions

- ** Contradictory Conditions**:
  - If any disease meets a contradictory condition based on available data, eliminate it from consideration.

- ** Necessary Conditions**:
  - List necessary conditions needed to diagnose the disease.
  - Ensure all necessary conditions for each disease are met. Eliminate any disease that fails to meet one or more necessary conditions.


#### 2b. Rule In Conditions

- **Sufficient/Pathognomonic Conditions**:
  - List if any sufficient or pathognomonic condition is met for the remaining diseases. If identified, confirm the diagnosis and set its probability to 100%.

#### 2c. Supportive Conditions

- **Assess Direct Support Conditions**:
  - Evaluate contextual and correlational support for each remaining disease. Adjust the likelihood percentages based on how well each disease fulfills these conditions.
- **Assess Indirect Support Conditions**:
  - Consider additional evidence that adds credibility to the diagnosis.

#### 2d. Evidence Strength

- **Separate Strong Evidence from Weak Evidence**:
  - **Strong Evidence**:
    - List Directly relevant, reliable, specific evidence with high diagnostic accuracy.
  - **Weak Evidence**:
    - List Indirect, less reliable evidence with lower diagnostic accuracy.

- Adjust the likelihood of each diagnosis based on the strength of the evidence.

---

## 3. Consider Comorbidity

- List potential combinations of diseases that could collectively explain the patient's symptoms.
- *Example:* "Consider concurrent viral infection and autoimmune reaction."

---


## 4. Clinical Decision Tools

- Recommend any applicable clinical decision support tools relevant to the case.
- Provide basic calculations and interpret the results within the context of the patient's presentation.
- Explain why these tools are helpful in the diagnostic process.

---

## 5. Summarize Findings

Now re list **each differential diagnosis** again, including those ruled out, provide the following:

- **Likelihood Percentage**: Assign a likelihood percentage to the disease based on evidence strength and support conditions.
- **Brief Explanation**: Summarize the reasoning 
- **Critical Information for Further Evaluation**:
  - **Follow-Up Questions**: Additional questions to ask the patient, with explanations of why they are important.
    - *Example:* "recent travel to assess exposure to endemic diseases."
  - **Specific Physical Exam Findings**: Targeted examination findings that could confirm or exclude the diagnosis, along with their significance.
    - *Example:* "Check for nuchal rigidity to evaluate for meningitis."
  - **Laboratory Tests**: Relevant tests to order, including reasons for their utility.
    - *Example:* "Order a complete blood count to look for signs of infection."
  - **Imaging Studies**: Appropriate imaging to perform, explaining how they would aid in diagnosis.
    - *Example:* "Obtain a chest X-ray to detect possible pneumonia."
  - **Clinical Decision Tools**: Recommend applicable tools and provide calculations or results if possible, explaining their relevance.
    - *Example:* "Use the Wells Score to assess the probability of deep vein thrombosis."

---
## 6. Medical Decision Making, Assesment and Plan
- Create a Medical Plan of structured medical problem list of interventions for each medical problem.
- Recommend medications or procedures for managing the patient's condition.
- Highlight any **CRITICAL ACTIONS** that must be taken or considered before dispositioning the patient. Exclude actions already done or mentioned as considered.
- Create the following sections:
    ## Medical Decision Making:
        [Summarize key findings from history, physical exam, and diagnostic studies]
        [Explain clinical reasoning process]
        [Discuss risk stratification for the patient's condition]
        [Include differential diagnoses:]
        - [List all diagnoses considered, from most to least likely, including those excluded early]
        - [For each diagnosis, briefly state supporting and contradicting evidence from the patient's presentation]
        - [Include probability estimates if discussed (very high, high, medium, low, or very low)]
        - [Explain why certain diagnoses were ruled out or require further workup]
        [Justify tests ordered, treatments given, and overall management plan]
        [Address any uncertainties or complexities in the case and how they were approached]
        [Explain how the differential informed the diagnostic and treatment plan]
    ## Assesment:
        [provide a summary statement of the patient and major problems]
        [Provide primary cause of chief complaint with reasoning]
        [Include any Clinical Decision Tools used]
    ## Plan:
        [Provide a Numbered list of problems identified, plan, include the reasoning discussed.]
        [highlight any **CRITICAL ACTIONS** that must be taken or considered before dispositioning the patient. Exclude actions already done or mentioned as considered.]
    ## Disposition:

## 7. Academic Insights
Provide interesting academic insights related to the differential diagnoses, such as mechanisms of action or practical medical nuances. Exclude basic educational points.

"""
#  Orgainize by DDX, then Questions, then Physical Exam, then Lab Tests, then Imaging Studies, then Clinical Decision Tools
summarize_case_by_test = """

Given the input text containing a patient case study, including sections like "History of Present Illness," "Review of Systems," "Physical Examination," and "Differential Diagnosis," perform the following tasks:

1. **Extract and Organize All Follow-Up Questions by Disease:**

   - Identify all follow-up questions mentioned for each diagnosis.
   - Organize these questions under headings for each disease.

2. **Extract and Organize All Specific Physical Exam Findings by Disease:**

   - Identify all specific physical exam findings recommended for further evaluation.
   - Organize these findings under headings for each disease.

3. **Extract and Organize All Laboratory Tests by Disease:**

   - Identify all laboratory tests suggested for further evaluation.
   - Organize these tests under headings for each disease.

4. **Extract and Organize All Imaging Studies by Disease:**

   - Identify all imaging studies recommended for further evaluation.
   - Organize these studies under headings for each disease.

5. **Extract and Organize All Clinical Decision Tools by Disease:**

   - Identify all clinical decision tools mentioned.
   - Organize these tools under headings for each disease.

**Output Format:**

Organize your findings under the following headings:

---

## Follow-Up Questions

**Hyperthyroidism (Graves' Disease or Toxic Nodular Goiter)**
- Weight changes, heat intolerance, and changes in energy levels

**Thyroiditis (Subacute or Silent)**
- Recent viral infections, neck pain severity

**Anxiety-related Palpitations**
- Recent stressors and anxiety symptoms

**Paroxysmal Supraventricular Tachycardia (PSVT)**
- Sudden onset and termination of rapid heartbeats

**Gastroesophageal Reflux Disease (GERD)**
- Heartburn, regurgitation, and positional worsening of symptoms

**Premature Ventricular Contractions (PVCs)**
- Family history of cardiac conditions

**Medication Side Effects (Celexa or Trazodone)**
- Timing of medication use and onset of symptoms

---

## Specific Physical Exam Findings

**Hyperthyroidism (Graves' Disease or Toxic Nodular Goiter)**
- Check for exophthalmos, lid lag, fine tremor, and thyroid bruit

**Thyroiditis (Subacute or Silent)**
- Assess thyroid tenderness and size

**Atrial Fibrillation (paroxysmal)**
- Listen for irregularly irregular rhythm during auscultation

**Mitral Valve Prolapse**
- Listen for mid-systolic click or late systolic murmur

**Anxiety-related Palpitations**
- Assess for signs of anxiety during examination

**Gastroesophageal Reflux Disease (GERD)**
- Check for epigastric tenderness

---

## Laboratory Tests

**Hyperthyroidism (Thyroid Dysfunction)**
- Thyroid function tests (TSH, Free T4, Free T3)
- Thyroid Stimulating Immunoglobulin (TSI)

**Thyroiditis (Subacute or Silent)**
- Erythrocyte Sedimentation Rate (ESR), C-Reactive Protein (CRP)

**Electrolyte Imbalance, Paroxysmal Supraventricular Tachycardia (PSVT), Atrial Fibrillation (paroxysmal)**
- Electrolyte panel

**Premature Ventricular Contractions (PVCs)**
- Cardiac enzymes to rule out myocardial damage

**General Screening**
- Complete Blood Count (CBC) and Basic Metabolic Panel (BMP)

---

## Imaging Studies

**Hyperthyroidism (Graves' Disease or Toxic Nodular Goiter, Thyroiditis)**
- Thyroid ultrasound
- Radioactive iodine uptake scan

**Premature Atrial Contractions (PACs), Premature Ventricular Contractions (PVCs), Atrial Fibrillation, Mitral Valve Prolapse**
- Echocardiogram to evaluate cardiac structure and function

**Paroxysmal Supraventricular Tachycardia (PSVT)**
- Event monitor or Holter monitor to capture episodes

**Premature Atrial Contractions (PACs)**
- 24-hour Holter monitor to quantify PACs

**Gastroesophageal Reflux Disease (GERD)**
- Upper GI series if symptoms persist

---

## Clinical Decision Tools

**Hyperthyroidism**
- Burch-Wartofsky Point Scale for thyroid storm risk assessment

**Anxiety-related Palpitations**
- Generalized Anxiety Disorder-7 (GAD-7) scale

**Atrial Fibrillation (paroxysmal)**
- CHA2DS2-VASc score if atrial fibrillation is confirmed

**Gastroesophageal Reflux Disease (GERD)**
- GERD Questionnaire (GerdQ)

**Medication Side Effects (Celexa or Trazodone, Medication-induced Hyperthyroidism)**
- Naranjo Adverse Drug Reaction Probability Scale

---

**Instructions:**

- Ensure all items extracted are directly from the input text.
- Under each heading, list relevant items grouped by disease in the format provided.
- Keep the output clear and minimal, without redundancy.
- Do not include extra information.
- Ensure diseases are used as section headings, and group related follow-up questions, physical exam findings, laboratory tests, imaging studies, and clinical decision tools under each disease accordingly.

**Note:** Your goal is to create a concise and organized summary that links each follow-up question, physical exam finding, laboratory test, imaging study, and clinical decision tool to the relevant diseases from the differential diagnosis. Display them grouped under each disease accordingly.
"""

# Group by follow up questions, physical exam findings, laboratory tests, imaging studies, clinical decision tools
summarize_case_grouped_by_test = """
Given the input text containing a patient case study, including sections like "History of Present Illness," "Review of Systems," "Physical Examination," and "Differential Diagnosis," perform the following tasks:

1. **Extract and List All Follow-Up Questions:**
   - Identify additional follow-up questions that were suggested after an initial assessment, focusing on those that were **not initially included** but are now deemed important for thorough evaluation.
   - Rank the questions in order of importance.
   - **Make the specific items bold**.
   - Remove unnecessary leading phrases like "Ask about"; use partial sentences instead.
   - Display affected diseases in parentheses after each specific item.

2. **Extract and List All Specific Physical Exam Findings:**
   - Identify additional specific physical examinations or special tests that were suggested for further evaluation after the initial physical examination.
   - Structure them by how they fit in a typical physical exam sequence (General, Skin, Hair, Nails, HEENT, Neck, Heart, Lungs, Abdomen, Back, Rectal, Extremities, Musculoskeletal, Neurologic, Psychiatric, Pelvic, Breast, Genitourinary).
   - **Make the specific items bold**.
   - Display affected diseases in parentheses after each specific item.

3. **Extract and List All Laboratory Tests:**
   - Identify additional laboratory tests that were recommended for further evaluation after the initial assessment.
   - Rank the tests in order of importance.
   - **Make the specific items bold**.
   - Display affected diseases in parentheses after each specific item.

4. **Extract and List All Imaging Studies:**
   - Identify additional imaging studies recommended after the initial evaluation.
   - Rank the studies in order of importance.
   - **Make the specific items bold**.
   - Display affected diseases in parentheses after each specific item.

5. **Extract and List All Clinical Decision Tools:**
   - Identify additional clinical decision tools that were suggested for use after the initial assessment.
   - Rank the tools in order of importance.
   - **Make the specific items bold**.
   - Display affected diseases in parentheses after each specific item.

**Output Format:**

Organize your findings under the following headings:

---

**Follow-Up Questions**

- **Weight changes, heat intolerance, and changes in energy levels** (Hyperthyroidism, Graves' Disease or Toxic Nodular Goiter, Thyroid Dysfunction)
- **Recent viral infections, neck pain severity** (Thyroiditis, Subacute or Silent)
- **Recent stressors and anxiety symptoms** (Anxiety-related Palpitations)
- **Sudden onset and termination of rapid heartbeats** (Paroxysmal Supraventricular Tachycardia, PSVT)
- **Heartburn, regurgitation, and positional worsening of symptoms** (Gastroesophageal Reflux Disease, GERD)
- **Family history of cardiac conditions** (Premature Ventricular Contractions, PVCs; Mitral Valve Prolapse)
- **Timing of medication use and onset of symptoms** (Medication Side Effects, Celexa or Trazodone; Medication-induced Hyperthyroidism)

---

**Physical Exam**

**General**
- **Assess for pallor or jaundice** (Anemia or Liver Dysfunction)

**HEENT**
- **Inspect for lid lag and lid retraction** (Hyperthyroidism)

**Neck**
- **Palpate for cervical lymphadenopathy** (Thyroiditis, Malignancy)

**Heart**
- **Assess for pulse deficit** (Atrial Fibrillation)

**Lungs**
- **Auscultate for added lung sounds** (Heart Failure, Pulmonary Edema)

**Abdomen**
- **Palpate for splenomegaly** (Chronic Infections, Hematologic Disorders)

---

**Laboratory Tests**
- **Thyroid function tests (TSH, Free T4, Free T3)** (Hyperthyroidism, Thyroid Dysfunction)
- **Erythrocyte Sedimentation Rate (ESR), C-Reactive Protein (CRP)** (Thyroiditis, Subacute or Silent)
- **Electrolyte panel** (Electrolyte Imbalance, Paroxysmal Supraventricular Tachycardia, PSVT, Atrial Fibrillation)
- **Thyroid Stimulating Immunoglobulin (TSI)** (Hyperthyroidism, Graves' Disease)

---

**Imaging Studies**
- **Thyroid ultrasound** (Hyperthyroidism, Graves' Disease or Toxic Nodular Goiter; Thyroiditis)
- **Radioactive iodine uptake scan** (Hyperthyroidism, to differentiate causes)

---

**Clinical Decision Tools**
- **Burch-Wartofsky Point Scale for thyroid storm risk assessment** (Hyperthyroidism)
- **Generalized Anxiety Disorder-7 (GAD-7) scale** (Anxiety-related Palpitations)

---

**Instructions:**
- Ensure all items extracted are **additional recommendations** after the initial assessment.
- Under each heading, list all relevant items in the format provided.
- Rank the items under each heading in order of importance.
- **Make the specific items bold**.
- Display affected diseases in parentheses after each specific item.
- Keep the output clear and minimal, without redundancy.
- For example, list follow-up questions by bullet points without numbering or additional labels.

**Note:** Your goal is to create a concise and organized summary that links **additional** follow-up questions, physical exam findings, laboratory tests, imaging studies, and clinical decision tools to the relevant diseases from the differential diagnosis. Rank the items in order of importance. **Make the specific items bold**, and display affected diseases in parentheses after each specific item.

---
"""

################################################ Cases ################################################

case_thyroid = """
    Use this transcript of the clinical encounter ''' Speaker 0: Okay. And this okay. Hi. Hello. Can you tell me what's going on?

    Speaker 1: I keep having these funny feeling in my chest.

    Speaker 0: Funny feeling in your chest. Okay. Can you tell me kinda more, like, when it started, what it feels like?

    Speaker 1: It feels like a bump that's kinda intermittent, and sometimes it's more, sometimes it's less. And that's been going on off and on for at least 5 days. Bothers me most at night, but I notice it during the day as well. Okay. Sometimes it makes me feel a bit short of breath.

    Speaker 0: Okay. And and where do you feel it in your chest?

    Speaker 1: It's right in the middle.

    Speaker 0: Right in the middle of your your substernal area. Okay. And does it radiate anywhere?

    Speaker 1: No. It's just like a a thump, and then maybe a minute later or 2 minutes later, I kinda feel another thump.

    Speaker 0: Okay. Alright. And so how long does that thump feel? Like, it was, like, a second?

    Speaker 1: Yeah.

    Speaker 0: Just a second. Okay. And and have you found anything that seems to, like, aggravate it that makes it go off, like activity or anything like that?

    Speaker 1: No. I went for a swim, and it was fine afterwards. I I noticed it most when I'm trying to fall asleep at night. It kinda keeps me from falling asleep. Okay.

    And then one time, I had spicy food for lunch, and then I noticed it more afterward.

    Speaker 0: Okay. But you don't get any burning sensation?

    Speaker 1: Where?

    Speaker 0: In in that with a thump? No. No. Okay.

    Speaker 1: Sensation with the thump.

    Speaker 0: Okay. Alright. And, um, do you have any other other symptoms, nausea, vomiting, sweating?

    Speaker 1: A couple times, it felt like a bit been a bit more sweaty, but not not no nausea, no vomiting, and it's not nothing nothing else. I've been eating eating fine.

    Speaker 0: Okay. How about do you get lightheaded or even pass out with that related to that thump?

    Speaker 1: No. With the thumb, I do feel like a little like, kinda I have to like, I'm I have to take a deep breath or something, but I haven't passed that.

    Speaker 0: Okay. Okay. Does it seem positional at all? Like, you mentioned nighttime laying down. Does it seem to happen more when you're more in the lying down position?

    Speaker 1: Yeah. Maybe.

    Speaker 0: Okay. And, um, alright. And then any, like, recent illnesses that you've noticed, coughs, colds, or any traumatic events, anything that you can think of that was add out of ordinary?

    Speaker 1: No. Not not really. I've been feeling okay in general. I mean, the kids are back at school, so, you know, maybe a little, you know, runny nose or sore throat or something a little bit, but nothing Yeah. Nothing major.

    Speaker 0: Okay. And, uh, sorry, sir. I haven't gotten, um, you know, your your history or sir? Is it a sir?

    Speaker 1: No. I'm a 43 year old woman.

    Speaker 0: A 43 year old woman. Alright. Can I'm sorry. I'm sorry, ma'am. Do you have any other medical history, surgical history?

    Speaker 1: I've been, uh, had testing in the past because my, uh, periods were, uh, irregular, but nothing really nothing really seemed to come out of that. And then I've had was, you know, pretty active when I was younger and had ACL surgery on both both knees. Um, but that's it. Otherwise, I've been been pretty healthy.

    Speaker 0: Okay. Do you take any medicines?

    Speaker 1: I take some trazodone sometimes to to sleep, and I've been on Celexa for some, uh, just kinda anxiety mood related stuff for a couple of years.

    Speaker 0: Okay. Do you take any supplements, energy drinks, anything that may kinda work you up a little bit?

    Speaker 1: Online, I buy stuff for, like, a a hair and nails supplement, but, um, I'm not sure what's what's all in that, but it's just it's just one of the online ones.

    Speaker 0: Okay. Alright. And is it is it a well known item, or is

    Speaker 1: it Yeah. From, like, some nature brand.

    Speaker 0: Okay. Okay. Alright. Okay. And have you ever seen a doctor for this before?

    Speaker 1: No. Um, this is the first visit.

    Speaker 0: Okay. And and sorry. What made you decide to finally come in today?

    Speaker 1: I just wasn't going away, and I felt like, well, maybe it's maybe it's something serious and I should come in.

    Speaker 0: Yeah. Okay. Alright. Okay. We're gonna do an exam.

    Can you tell me what your vitals are and how you look and all that stuff?

    Speaker 1: Look generally healthy, like, not toxic or anything. And vitals,

    Speaker 0: You can say

    Speaker 1: Blood pressure, systolic a little bit on the high side. Heart rate is also a little bit high, and it's irregular.

    Speaker 0: Over a 100?

    Speaker 1: What's that?

    Speaker 0: Is it is it over a 100?

    Speaker 1: Yeah. Oh. It's like just into the into the 100. It's like 108 or 100 and 10 or something like that. Okay.

    And but mostly, uh, not it's not it doesn't feel like irregularly irregularly, like, AFib, just like an extra some kinda extra systemic thing happening once in a while.

    Speaker 0: Okay.

    Speaker 1: And, you know, BMI 28. Normal temp. So afebrile. And, yeah, nothing on

    Speaker 0: Exam?

    Speaker 1: Inspection. Nothing else super, um, super dramatic. Palms are maybe a little bit, uh, sweaty.

    Speaker 0: Yeah. Oh, okay. And, um, looks like we got an EKG. Do you know what your EKG said?

    Speaker 1: It there's a a occasional supraventricular extrasystoles.

    Speaker 0: Okay. Alright. Okay. But they're like, your intervals and everything seem to be okay?

    Speaker 1: Yeah. Yeah. Otherwise, nothing Okay. No, uh, no, you know, it's normal. The rest are rest is sort of a normal PQRS.

    Nothing Okay. Other than some supraventricular extracelystole.
    """

case_thyroid2_output = """
Certainly, I'll work on the patient data based on the provided transcript. Please wait while I am working on the patient data...
<workup_patient>
1. Initial Assessment
History of Present Illness (HPI):
The patient is a 43-year-old female presenting with a chief complaint of "funny feeling" in her chest. The sensation is described as a "thump" or "bump" that is intermittent, occurring for at least 5 days. It is more noticeable at night, interfering with sleep, but also present during the day. The feeling is localized to the middle of the chest (substernal area) and does not radiate. Each episode lasts about a second and may recur after 1-2 minutes. The patient reports associated shortness of breath at times. Swimming does not aggravate the symptoms, but spicy food seemed to increase the frequency. The patient denies any burning sensation, nausea, or vomiting. Occasional sweating is reported. The patient feels the need to take a deep breath with the "thump" but denies syncope or presyncope.
Review of Systems (ROS):
- Cardiovascular: Positive for palpitations, shortness of breath. Negative for chest pain, syncope.
- Respiratory: Positive for mild dyspnea. Negative for cough.
- Gastrointestinal: Negative for nausea, vomiting. Positive for increased symptoms after spicy food.
- Neurological: Negative for dizziness, syncope.
- General: Positive for occasional sweating. Negative for fever.
- ENT: Positive for mild runny nose and sore throat (attributed to children returning to school).
Past Medical History (PMH):
- History of irregular menstrual periods (evaluated in the past, no specific diagnosis mentioned)
- Anxiety/mood disorder (on treatment)
Past Surgical History (PSH):
- ACL surgery on both knees
Family History (FH):
Not provided in the transcript.
Social History (SH):
- Mother with school-age children
- Swimming for exercise
Medications:
- Trazodone (as needed for sleep)
- Celexa (for anxiety/mood, for a couple of years)
- Hair and nail supplement (online purchase, nature brand)
Allergies:
Not provided in the transcript.
Physical Examination:
- General: Patient appears generally healthy, not toxic
- Cardiovascular: Irregular heart rhythm noted
- Skin: Palms slightly sweaty
- No other significant findings reported on examination
Vital Signs:
- Blood Pressure: Systolic slightly elevated (exact number not provided)
- Heart Rate: 108-110 bpm, irregular
- Temperature: Afebrile
- BMI: 28
2. Differential Diagnosis (DDX)
1. Premature Atrial Contractions (PACs)
Likelihood: 90%
Explanation: The patient's symptoms of intermittent "thumps" in the chest, irregular heart rhythm on exam, and EKG showing supraventricular extrasystoles strongly support this diagnosis.
Critical Information for Further Evaluation:
- Follow-Up Questions: Frequency of episodes, associated triggers (caffeine, stress, alcohol)
- Physical Exam Findings: Auscultation for irregular rhythm or extra beats
- Laboratory Tests: Thyroid function tests, electrolytes (especially potassium and magnesium)
- Imaging Studies: Echocardiogram to rule out structural heart disease
- Clinical Decision Tools: 24-hour Holter monitor to quantify PAC burden
2. Gastroesophageal Reflux Disease (GERD)
Likelihood: 40%
Explanation: The patient's symptoms worsen with spicy food and when lying down, which is consistent with GERD. However, the absence of typical burning sensation makes this less likely as the primary cause.
Critical Information for Further Evaluation:
- Follow-Up Questions: Presence of heartburn, regurgitation, or sour taste in mouth
- Physical Exam Findings: Epigastric tenderness
- Laboratory Tests: None specific, but could consider H. pylori testing if indicated
- Imaging Studies: Upper GI series if symptoms persist
- Clinical Decision Tools: GERD questionnaire (e.g., GerdQ)
3. Anxiety-related Palpitations
Likelihood: 30%
Explanation: The patient has a history of anxiety and is on medication for mood disorders. Anxiety can cause palpitations and sweating.
Critical Information for Further Evaluation:
- Follow-Up Questions: Recent stressors, changes in anxiety symptoms
- Physical Exam Findings: Signs of anxiety (restlessness, tremor)
- Laboratory Tests: None specific
- Imaging Studies: None specific
- Clinical Decision Tools: GAD-7 or Beck Anxiety Inventory
4. Paroxysmal Supraventricular Tachycardia (PSVT)
Likelihood: 20%
Explanation: While the EKG shows supraventricular extrasystoles, the patient's symptoms don't typically last long enough to suggest sustained PSVT episodes.
Critical Information for Further Evaluation:
- Follow-Up Questions: Any sudden onset rapid heartbeats lasting minutes
- Physical Exam Findings: Auscultation during an episode if possible
- Laboratory Tests: Electrolytes, TSH
- Imaging Studies: Echocardiogram
- Clinical Decision Tools: 24-hour Holter monitor or event recorder
5. Thyroid Dysfunction
Likelihood: 15%
Explanation: Thyroid disorders can cause palpitations and sweating. The patient's slightly elevated heart rate could be consistent with hyperthyroidism.
Critical Information for Further Evaluation:
- Follow-Up Questions: Recent weight changes, heat/cold intolerance, changes in energy levels
- Physical Exam Findings: Thyroid examination, eye changes
- Laboratory Tests: TSH, Free T4, Free T3
- Imaging Studies: Thyroid ultrasound if abnormalities detected on exam
- Clinical Decision Tools: Thyroid symptom questionnaire
6. Medication Side Effect (Celexa or Trazodone)
Likelihood: 10%
Explanation: Both medications can potentially cause palpitations as a side effect, but the timing doesn't correlate with medication initiation.
Critical Information for Further Evaluation:
- Follow-Up Questions: Timing of symptom onset in relation to medication use, any recent dose changes
- Physical Exam Findings: None specific
- Laboratory Tests: Drug levels if applicable
- Imaging Studies: None specific
- Clinical Decision Tools: Naranjo Adverse Drug Reaction Probability Scale
3. Consider Comorbidity
Consider the possibility of PACs exacerbated by underlying GERD or anxiety.
4. Clinical Decision Tools
- 24-hour Holter monitor: To quantify PAC burden and detect any sustained arrhythmias
- GERD questionnaire (GerdQ): To assess likelihood of GERD
- GAD-7 or Beck Anxiety Inventory: To evaluate anxiety levels
5. Medical Decision Making, Assessment, and Plan
Medical Decision Making:
The patient presents with intermittent palpitations described as "thumps" in the chest, occurring for at least 5 days. The physical examination reveals an irregular heart rhythm, and the EKG shows supraventricular extrasystoles. These findings strongly suggest Premature Atrial Contractions (PACs) as the primary diagnosis.
However, the exacerbation of symptoms with spicy food and when lying down raises the possibility of GERD as a contributing factor. The patient's history of anxiety and current use of anxiety medication also suggests a potential anxiety component to the symptoms.
The slightly elevated blood pressure and heart rate warrant further investigation, particularly to rule out thyroid dysfunction. The irregular heart rhythm on examination correlates with the EKG findings of supraventricular extrasystoles, supporting the diagnosis of PACs.
While PSVT is in the differential, the short duration of symptoms makes this less likely. Medication side effects are considered but deemed less probable due to the timing of symptom onset.
The plan includes further diagnostic tests to confirm PACs, evaluate for structural heart disease, and investigate potential contributing factors such as GERD and thyroid dysfunction.
Assessment:
43-year-old female presenting with palpitations, most likely due to Premature Atrial Contractions (PACs), with possible contributions from GERD and/or anxiety.
Plan:
1. Arrhythmia Evaluation:
- Order 24-hour Holter monitor to quantify PAC burden and detect any sustained arrhythmias
- Perform echocardiogram to rule out structural heart disease
2. Laboratory Tests:
- Complete blood count (CBC)
- Comprehensive metabolic panel (CMP) including electrolytes
- Thyroid function tests (TSH, Free T4)
3. GERD Evaluation:
- Provide GERD questionnaire (GerdQ)
- Recommend lifestyle modifications: avoid spicy foods, elevate head of bed
- Consider trial of proton pump inhibitor if GERD symptoms are significant
4. Anxiety Management:
- Administer GAD-7 or Beck Anxiety Inventory
- Discuss current anxiety symptoms and effectiveness of current medication
5. Medication Review:
- Review current medications, including the online hair and nail supplement
- Educate on avoiding potential triggers (caffeine, alcohol)
6. Follow-up:
- Schedule follow-up appointment in 1-2 weeks to review test results and reassess symptoms
CRITICAL ACTIONS:
- Perform ECG to confirm PACs and rule out other arrhythmias
- Educate patient on when to seek immediate medical attention (prolonged palpitations, chest pain, syncope)
Disposition:
Discharge home with close follow-up and pending outpatient tests as outlined in the plan.
6. Academic Insights:
- PACs are often benign but can be associated with an increased risk of atrial fibrillation in some patients, particularly if frequent (>100/day).
- The relationship between GERD and cardiac symptoms, sometimes referred to as "linked angina," can complicate diagnosis and may require empiric treatment of GERD to differentiate.
- Anxiety can lower the threshold for perceiving normal physiological sensations as abnormal, potentially amplifying the patient's awareness of PACs.
</workup_patient>
"""

case_86f_chest_pain = """
Use this transcript of the clinical encounter ''' Speaker 0: Sure. Yeah. What's your husband's name? Robert. Robert.

So what's going on? What's bringing you in? What's bringing you here?

Speaker 1: Well, I'm having, you know, the chest pain, and it was going through to the back.

Speaker 0: You're okay.

Speaker 1: Probably a couple of weeks now it's been going on. So yesterday, my my heart doctor sent me in to get an X-ray of

Speaker 0: it. Yeah.

Speaker 1: That all came back. But the pain's not going away.

Speaker 0: Gotcha.

Speaker 1: And he wants to have Aethere.

Speaker 0: Yeah. And

Speaker 1: he wants to put me on a different medicine to the atrium. Sorry. The one that Yeah. Keep it in sync because it was out just a few minutes ago. It was out.

Speaker 0: Okay. Okay.

Speaker 1: I guess he wants to make sure that this isn't something serious.

Speaker 0: Sure. Sure. Okay. Let's talk more about the pain. Do you feel the pain right now?

Yeah. On on a 1 to 10?

Speaker 1: I'm pretty good with pain, so maybe 5.

Speaker 0: A 5. Okay. What does that feel like?

Speaker 1: Pressure plus Press. Okay. Have, like, a indigestion.

Speaker 0: Indigestion feeling? Okay. Alright. And then you feel it. It goes into your shoulder Yeah.

In the back of your shoulder there. Okay. Does it go down your arm or up your neck at all?

Speaker 1: Back of the neck. Right. Yeah. In

Speaker 0: the back of your neck a little bit. Okay. Okay. Alright. Any nausea?

No.

Speaker 1: Just like kinda indigestion.

Speaker 0: Indigestion. How about sweats? Like, you feel like you're sweating or anything like that? No. No.

Okay. And you've been is it getting worse or just still not going away?

Speaker 1: It's just not going away.

Speaker 0: Gotcha. Have you noticed anything that makes it worse? Like walking?

Speaker 1: No.

Speaker 0: No. Walking doesn't seem to make it worse?

Speaker 1: I think it gets worse when you lay down at night.

Speaker 0: When you lay down at night. Okay. Alright. How about eating? Does eating do anything?

Does taking a deep breath do anything? No. Okay. Alright. So you feel like you're eating and drinking okay?

Yeah. Okay. Alright. Alright.

Speaker 1: When you were ironing, you were sweating pretty much. Yeah.

Speaker 0: Did you have did when you were ironing and sweating, did you remember notice if your pain was worse when you were ironing?

Speaker 1: Yeah. It was real bad because I thought I only have one more item that I am am I gonna get through this? So I guess it must have been worse.

Speaker 0: Okay. Gotcha. Okay. Alright. So we gotta do some do some tests.

Oh, one more question. Have you ever had a heart attack before? No. Okay. Okay.

Alright.

Speaker 1: Not to my knowledge.

Speaker 0: Okay. Have you ever had pain like this before the last cup couple weeks that this has been going on?

Speaker 1: I've had it before, but something that would maybe I've had it for maybe half the day, and

Speaker 0: then it's gone.

Speaker 1: Okay. The years ago, I took her to Saint Joseph's in Yeah.

Speaker 0: Yeah.

Speaker 1: That's was the Kaiser facility. She the cartilage around the heart

Speaker 0: was inflamed? Yes. Yeah. Tostachondritis probably is what it okay. Okay.

Alright. So we're gonna do some tests.

Speaker 1: Okay? Okay.

Speaker 0: I don't like how it's not getting any better. Okay? And now that you can't do, uh, the ironing, that's a concern.

Speaker 1: And then, you know, it's funny because I didn't contribute it to Yeah. The pain was getting so bad.

Speaker 0: Yeah.

Speaker 1: I just it didn't. You know?

Speaker 0: Yeah.

Speaker 1: Because I have a bad backache.

Speaker 0: Sure. Sure. Sure. Okay. And the back the back pains that you usually you get, where in the back do you get those pains?

Speaker 1: Oh, that's

Speaker 0: That's a low back. Low back. Okay. Not an upper back thing.

Speaker 1: Yeah. Okay. She's got 3 surgeries on her.

Speaker 0: Gotcha. Gotcha. Gotcha. Okay. Alright.

So we're gonna do some tests. Okay? I'm gonna make sure everything is is going on. But even if this first round of tests are okay, I because of the it sounds concerning, I would like to do some advanced tests, but those advanced tests require being admitted to the hospital for overnight. Is that okay?

Yeah. The the thing is is

Speaker 1: real bad. I get panic attacks.

Speaker 0: We can give you medicine to help with panic attacks. The thing is is there is a chance that your blood vessels in your heart are very narrow, and that I

Speaker 1: love blood thinners.

Speaker 0: I know. That helps. That helps. But you can still get heart attacks. So it this could be where it's it's very narrow that you're any chance you might be getting a heart attack.

And so these advanced tests would know if you have these very nestled blood vessels. Because ideally, we catch this before you have a major heart attack. Right? And in order to do that, we may need to do these more advanced tests that means you need to stay the night. But

Speaker 1: you won't know after you do some

Speaker 0: other tests. These first round of tests will will will tell if you've had a heart attack, but the 2nd round of test will say if you're at high risk of having a heart attack any day. Okay? I know it's not something here. Let's just we just put that on the table.

You don't have to make any decisions right now. We'll just go through the 1st round of the test. Okay? Okay. And then we'll talk later after that.

Does this sound good? Okay. Okay. Alright. Sound good, sir?

Speaker 1: Yes.

Speaker 0: Okay. Have you had any aspirin today?

Speaker 1: No. Okay.

Speaker 0: We're gonna give you some aspirin while we're waiting.

Speaker 1: I'm gonna take it.

Speaker 0: Okay. Alright. We're gonna give you some, though, today, okay, while we're working this up. It's standard treatment to make sure your heart's okay. Alright?

Prevention.

Speaker 1: I didn't think I was supposed to take aspirin. You are for this.

Speaker 0: You are for this. You are for this. Okay? Okay.

Speaker 1: Doctor. Wayne stopped the aspirin a lot.'''
  
  """

sample_result = """
## 1. Initial Assessment
```HISTORY OF PRESENT ILLNESS```
A 43-year-old female presents with a chief complaint of a "funny feeling" in her chest that has been occurring intermittently for at least 5 days. The patient describes it as a "thump" feeling in the middle of her chest, lasting about a second, occurring every 1-2 minutes. It's most bothersome at night, interfering with sleep, but also noticeable during the day. Sometimes it's associated with a feeling of shortness of breath. The patient reports no clear aggravating factors, though she noticed it more after eating spicy food once. She denies any burning sensation, nausea, or vomiting. The patient mentions occasionally feeling more sweaty with the episodes. She reports feeling the need to take a deep breath with the "thump" but denies lightheadedness or syncope. The symptoms seem to be more noticeable when lying down. There's no recent history of significant illness or trauma, though she mentions minor cold symptoms (runny nose, sore throat) possibly related to her children returning to school.
```REVIEW OF SYSTEMS```
- Cardiovascular: Positive for palpitations ("thumping" sensation in chest), occasional associated shortness of breath
- Respiratory: Denies cough, mentions mild shortness of breath with palpitations
- Gastrointestinal: Denies nausea, vomiting, or burning sensation; notes increased palpitations after spicy food once
- Neurological: Denies lightheadedness or syncope
- General: Reports occasional increased sweating with episodes
- ENT: Mentions minor cold symptoms (runny nose, sore throat)
```PHYSICAL EXAMINATION```
- General: Patient appears generally healthy, not in acute distress
- Cardiovascular: Heart rate is elevated (108-110 bpm) and irregular, with occasional extra beats noted
- Skin: Palms noted to be slightly sweaty
- No other significant physical exam findings reported
Vitals:
- Blood Pressure: Systolic slightly elevated (exact value not provided)
- Heart Rate: 108-110 bpm, irregular
- Temperature: Afebrile
- BMI: 28
---
## 2. Differential Diagnosis (DDX)
1. Premature Atrial Contractions (PACs)
2. Premature Ventricular Contractions (PVCs)
3. Paroxysmal Supraventricular Tachycardia (PSVT)
4. Atrial Fibrillation
5. Anxiety-induced Palpitations
6. Gastroesophageal Reflux Disease (GERD)
7. Thyroid Dysfunction (e.g., Hyperthyroidism)
8. Electrolyte Imbalance
9. Medication Side Effect (e.g., from Celexa or Trazodone)
10. Stimulant Effect from Supplements
### For Each Diagnosis:
1. Premature Atrial Contractions (PACs)
- **Likelihood: 90%**
- **Explanation**: The patient's description of intermittent "thumps" in the chest, irregular heart rhythm on exam, and EKG showing occasional supraventricular extrasystoles strongly support this diagnosis.
- **Critical Information**:
- Follow-Up Questions: Ask about caffeine intake, stress levels, and sleep quality.
- Physical Exam: Listen for irregular heart sounds during auscultation.
- Laboratory Tests: Consider thyroid function tests and electrolyte panel.
- Imaging Studies: Echocardiogram to rule out structural heart disease.
- Clinical Decision Tools: N/A for PACs specifically.
2. Premature Ventricular Contractions (PVCs)
- **Likelihood: 30%**
- **Explanation**: While the symptoms are similar to PACs, the EKG specifically mentioned supraventricular extrasystoles, making PVCs less likely.
- **Critical Information**:
- Follow-Up Questions: Ask about family history of heart disease.
- Physical Exam: Assess for signs of underlying heart disease.
- Laboratory Tests: Cardiac enzymes to rule out myocardial injury.
- Imaging Studies: Consider Holter monitor for 24-48 hours.
- Clinical Decision Tools: N/A for PVCs specifically.
3. Paroxysmal Supraventricular Tachycardia (PSVT)
- **Likelihood: 20%**
- **Explanation**: While the patient has supraventricular extrasystoles, the description doesn't fit typical PSVT episodes, which are usually more sustained.
- **Critical Information**:
- Follow-Up Questions: Ask about sudden onset rapid heartbeats lasting minutes to hours.
- Physical Exam: Check for sudden changes in heart rate during examination.
- Laboratory Tests: None specific, but consider electrolytes.
- Imaging Studies: Event monitor for longer-term heart rhythm assessment.
- Clinical Decision Tools: N/A for PSVT specifically.
4. Atrial Fibrillation
- **Likelihood: 10%**
- **Explanation**: While the heart rhythm is described as irregular, the EKG doesn't mention atrial fibrillation, and the symptoms don't typically fit.
- **Critical Information**:
- Follow-Up Questions: Ask about persistent irregular heartbeats or palpitations.
- Physical Exam: Listen for irregularly irregular heart rhythm.
- Laboratory Tests: Check thyroid function and electrolytes.
- Imaging Studies: Echocardiogram to assess for structural heart disease.
- Clinical Decision Tools: CHA2DS2-VASc score if AFib is confirmed.
5. Anxiety-induced Palpitations
- **Likelihood: 60%**
- **Explanation**: Patient has a history of anxiety and is on Celexa. Symptoms worsen at night when trying to sleep, which is common with anxiety.
- **Critical Information**:
- Follow-Up Questions: Ask about recent stressors, panic attacks, or changes in anxiety symptoms.
- Physical Exam: Assess for signs of anxiety during the visit.
- Laboratory Tests: Consider thyroid function tests.
- Imaging Studies: None specific to anxiety.
- Clinical Decision Tools: GAD-7 or Beck Anxiety Inventory to assess anxiety levels.
6. Gastroesophageal Reflux Disease (GERD)
- **Likelihood: 20%**
- **Explanation**: Patient noticed increased symptoms after spicy food, but denies typical burning sensation.
- **Critical Information**:
- Follow-Up Questions: Ask about heartburn, regurgitation, or worsening when lying down.
- Physical Exam: Check for epigastric tenderness.
- Laboratory Tests: None specific for GERD.
- Imaging Studies: Consider upper GI series if symptoms persist.
- Clinical Decision Tools: GerdQ questionnaire.
7. Thyroid Dysfunction (e.g., Hyperthyroidism)
- **Likelihood: 30%**
- **Explanation**: Some symptoms (palpitations, sweating) could be consistent with hyperthyroidism.
- **Critical Information**:
- Follow-Up Questions: Ask about weight changes, heat intolerance, or changes in energy levels.
- Physical Exam: Check for thyroid enlargement, tremors, or exophthalmos.
- Laboratory Tests: Thyroid function tests (TSH, Free T4, Free T3).
- Imaging Studies: Thyroid ultrasound if physical exam is concerning.
- Clinical Decision Tools: Burch-Wartofsky Point Scale for thyroid storm if severe hyperthyroidism is suspected.
8. Electrolyte Imbalance
- **Likelihood: 15%**
- **Explanation**: Electrolyte imbalances can cause palpitations, but there's no clear history suggesting this.
- **Critical Information**:
- Follow-Up Questions: Ask about changes in diet, fluid intake, or use of diuretics.
- Physical Exam: Check for signs of dehydration or edema.
- Laboratory Tests: Comprehensive metabolic panel, focusing on potassium, magnesium, and calcium levels.
- Imaging Studies: None specific for electrolyte imbalance.
- Clinical Decision Tools: N/A for electrolyte imbalances specifically.
9. Medication Side Effect (e.g., from Celexa or Trazodone)
- **Likelihood: 40%**
- **Explanation**: Both Celexa and Trazodone can potentially cause palpitations as a side effect.
- **Critical Information**:
- Follow-Up Questions: Ask about the timing of medication use and onset of symptoms, any recent dosage changes.
- Physical Exam: No specific findings for medication side effects.
- Laboratory Tests: Consider drug levels if applicable.
- Imaging Studies: None specific for medication side effects.
- Clinical Decision Tools: Naranjo Adverse Drug Reaction Probability Scale.
10. Stimulant Effect from Supplements
- **Likelihood: 25%**
- **Explanation**: Patient reports taking hair and nail supplements, which could potentially contain stimulants.
- **Critical Information**:
- Follow-Up Questions: Ask for specific brand and ingredients of the supplement, timing of use relative to symptoms.
- Physical Exam: Look for signs of stimulant use (e.g., dilated pupils, hypertension).
- Laboratory Tests: Consider urine drug screen if concerned about undisclosed stimulant use.
- Imaging Studies: None specific for supplement effects.
- Clinical Decision Tools: N/A for supplement effects specifically.
---
## 3. Consider Comorbidity
Given the patient's history of anxiety and the current symptoms, it's possible that there's a combination of anxiety-induced palpitations and actual cardiac arrhythmia (likely PACs). The anxiety could be exacerbating the perception of the PACs, making them more noticeable and distressing, especially at night when trying to sleep.
---
## 4. Summarize Findings
The most likely diagnosis appears to be Premature Atrial Contractions (PACs), possibly exacerbated by underlying anxiety. The patient's description of intermittent "thumps" in the chest, irregular heart rhythm on exam, and EKG showing occasional supraventricular extrasystoles strongly support this diagnosis. However, anxiety-induced palpitations are also a strong possibility given the patient's history and the nature of the symptoms.
---
## 5. Clinical Decision Tools
1. **GAD-7 (Generalized Anxiety Disorder 7-item scale)**: This would be useful to assess the patient's current level of anxiety, which could be contributing to or exacerbating the symptoms.
2. **CHA2DS2-VASc score**: While atrial fibrillation is less likely, if it's confirmed on further testing, this score would be important for assessing stroke risk.
3. **Naranjo Adverse Drug Reaction Probability Scale**: This could be used to evaluate the likelihood that the patient's symptoms are related to her medications (Celexa or Trazodone).
4. **GerdQ questionnaire**: This could help evaluate the possibility of GERD, which was mentioned as a possible differential diagnosis.
These tools would provide additional structured information to guide further management and treatment decisions.
"""

case_10M_mexican_URI = """
History of Present Illness:
Carlos, a 10-year-old Mexican-American boy, presents to the clinic with his mother, Maria. He has had cold symptoms for 3 days, including rhinorrhea, cough, and low-grade fever. Maria reports that Carlos has been more fatigued than usual and has had a decreased appetite. She is interested in treating him at home with traditional Mexican remedies. Maria expresses a strong preference for natural and cultural treatments over conventional medicine.

Past Medical History:
- No significant past medical history
- Up to date on vaccinations
- No known allergies

Family History:
- Father: Type 2 Diabetes
- Maternal grandmother: Hypertension

Social History:
- Lives with both parents and two younger siblings
- Attends 5th grade at local elementary school
- No exposure to tobacco smoke at home

Review of Systems:
- General: Fatigue, decreased appetite
- HEENT: Rhinorrhea, sore throat
- Respiratory: Dry cough, no shortness of breath
- Cardiovascular: No chest pain
- Gastrointestinal: No nausea, vomiting, or diarrhea
- Skin: No rashes

Physical Examination:
- Vital Signs: Temp 38.2°C (100.8°F), HR 92, RR 20, BP 110/70, SpO2 98% on room air
- General: Alert, mildly fatigued-appearing boy
- HEENT: Mild pharyngeal erythema, no exudates. Clear rhinorrhea. TMs intact bilaterally.
- Neck: No lymphadenopathy
- Lungs: Clear to auscultation bilaterally, no wheezes or crackles
- Cardiovascular: Regular rate and rhythm, no murmurs
- Abdomen: Soft, non-tender, no organomegaly
- Skin: No rashes or lesions

"""

case_50F_native_american_flu = """
History of Present Illness:
Sarah, a 50-year-old Native American woman from the Navajo Nation, presents to the clinic with a 5-day history of fever, body aches, fatigue, and dry cough. She reports feeling progressively worse over the past few days, with difficulty performing daily activities due to fatigue. Sarah expresses a strong interest in incorporating traditional Native American healing practices and natural remedies into her treatment plan.

Past Medical History:
- Type 2 Diabetes Mellitus (diagnosed 8 years ago)
- Hypertension (diagnosed 5 years ago)
- Obesity (BMI 32)
- History of recurrent urinary tract infections

Medications:
- Metformin 1000mg BID
- Lisinopril 10mg daily
- Aspirin 81mg daily

Allergies: Penicillin (rash)

Family History:
- Father: Type 2 Diabetes, died of myocardial infarction at age 62
- Mother: Breast cancer survivor, currently 75 years old
- Sister: Rheumatoid arthritis

Social History:
- Lives on the Navajo reservation with her husband
- Works as a teacher at a local elementary school
- Non-smoker, occasional alcohol use (1-2 drinks per week)
- Practices traditional Navajo ceremonies and healing rituals

Review of Systems:
- General: Fever, fatigue, body aches
- Respiratory: Dry cough, mild shortness of breath with exertion
- ENT: Sore throat, nasal congestion
- Gastrointestinal: Decreased appetite, no nausea or vomiting
- Musculoskeletal: Generalized myalgia
- Neurological: Mild headache

Physical Examination:
- Vital Signs: Temp 38.9°C (102°F), HR 98, RR 20, BP 145/90, SpO2 96% on room air
- General: Alert, fatigued-appearing woman
- HEENT: Mild pharyngeal erythema, no exudates. Nasal mucosa erythematous and edematous
- Neck: No lymphadenopathy
- Lungs: Scattered rhonchi bilaterally, no wheezes or crackles
- Cardiovascular: Regular rate and rhythm, no murmurs
- Abdomen: Soft, non-tender, no organomegaly
- Extremities: No edema, pulses intact
"""

case_45F_saddle_PE = """## Patient Information
- Name: Jane Goodall, 45-year-old female
- No significant past medical history
- Recent knee surgery 2 weeks ago

## Chief Complaint
"Sudden severe chest pain and difficulty breathing"

## History of Present Illness
The patient presents to the emergency department with sudden onset of severe chest pain and shortness of breath that started approximately 1 hour ago. She describes the pain as sharp, constant, and worsening with inspiration. The patient reports feeling lightheaded and anxious. She denies any fever, cough, or leg pain.

## Relevant Medical History
- Knee arthroscopy 2 weeks ago
- No history of clotting disorders or cardiovascular disease
- No recent long-distance travel

## Medications
- Acetaminophen PRN for post-operative pain

## Social History
- Non-smoker
- Occasional alcohol use
- Sedentary lifestyle, especially since surgery

## Physical Examination
- Vital Signs:
  - BP: 90/60 mmHg
  - HR: 120 bpm
  - RR: 28/min
  - O2 Sat: 88% on room air
  - Temp: 37.2°C (98.9°F)
- General: Anxious, diaphoretic, in visible distress
- Cardiovascular: Tachycardic, regular rhythm, no murmurs
- Respiratory: Tachypneic, decreased breath sounds bilaterally
- Extremities: Right knee with well-healing surgical scar, no calf tenderness or edema

## Initial Workup
- ECG: Sinus tachycardia, right axis deviation, S1Q3T3 pattern
"""
############################################### Note Writer ############################################################################################################

note_writer_system_pediatric_clinic_note = """
    
    I may ask general questions. If I do, just answer those. However, if I ask you to write a note, please follow these instructions:

    **Task**: Write a comprehensive **Pediatric Clinic Note** for the patient encounter we discussed. Address the patient as "the patient" or by their first name if appropriate, and incorporate the following guidelines:

    1. **Note Sections**:
    - If I request only a specific section of the note, provide only that section.
    - If not specified, include all of the following sections:
        - **Patient Information**
        - **Date and Time of Visit**
        - **Chief Complaint**
        - **History of Present Illness**
        - **Review of Systems**
        - **Past Medical History**
        - **Family History**
        - **Social History**
        - **Medications**
        - **Allergies**
        - **Immunizations**
        - **Growth and Development**
        - **Physical Examination**
        - **Assessment**
        - **Differential Diagnosis**
        - **Plan**
        - **ICD Billing Codes Consideration**
        - **Physician's Signature and Credentials**

    2. **Details to Include**:
    - For the **Review of Systems** and **Physical Examination**, fill in expected positive and negative findings not explicitly mentioned, based on standard pediatric practice.
    - Do **not** include any **laboratory results** or **imaging findings** unless they were specifically provided during our discussion.
    - If any required information is missing, insert triple asterisks (***) in the appropriate section.

    3. **Differential Diagnosis**:
    - Include every condition or disease considered in the **Differential Diagnosis**, including those that were excluded early.
    - Provide a brief explanation for each diagnosis, including supporting and contradicting evidence, and the reasoning for ruling them out or keeping them in the differential.
    - Provide a qualitative likelihood assessment for each diagnosis (e.g., very high, high, medium, low, very low).
    - The more comprehensive the differential diagnosis, the better.

    4. **ICD Billing Codes**:
    - At the end of the note, under **ICD Billing Codes Consideration**, suggest appropriate ICD-10 codes that correspond to the diagnoses and conditions mentioned in the note.
    - Ensure the codes are accurate and relevant to the patient's presentation and your clinical assessment.

    5. **Style and Formatting**:
    - Use **standard medical terminology and abbreviations**.
    - Format the note in a clear, organized manner consistent with **pediatric clinic documentation practices**.

    6. **Growth and Development**:
    - Include any relevant **developmental milestones** or concerns, and note if the patient is meeting age-appropriate milestones.

    7. **Preventive Care and Education**:
    - Include any **anticipatory guidance**, **preventive care considerations**, or **parental education** relevant to the patient's age and developmental stage.

    8. **Transcription Consent**:
    - ONLY if a transcription is provided, add a statement at the end of the note indicating that the parent or guardian consented to the use of AI transcription technology.

    9. **Confidentiality**:
    - Ensure patient confidentiality by avoiding the use of any real patient identifiers unless they were provided for the purpose of this note.

    **Note**: Please generate the **Pediatric Clinic Note** based on the patient case we discussed, adhering strictly to these instructions. Place triple asterisks (***) where information is missing. Structure the note according to the template provided within the triple backticks below.

    ```
    PATIENT INFORMATION:
    DATE AND TIME OF VISIT:
    CHIEF COMPLAINT:
    HISTORY OF PRESENT ILLNESS:
    REVIEW OF SYSTEMS:
    PAST MEDICAL HISTORY:
    FAMILY HISTORY:
    SOCIAL HISTORY:
    MEDICATIONS:
    ALLERGIES:
    IMMUNIZATIONS:
    GROWTH AND DEVELOPMENT:
    PHYSICAL EXAMINATION:
    ASSESSMENT:
    DIFFERENTIAL DIAGNOSIS:
    PLAN:
    PHYSICIAN'S SIGNATURE AND CREDENTIALS:
    ICD-10 BILLING CODES CONSIDERATION:
    ```

    """

note_writer_system_family_medicine_clinic_note_natural = """
I may ask general questions. If I do, just answer those. However, if I ask you to write a note, please follow these instructions:

Task: Write a comprehensive Family Medicine Clinic Note for the patient encounter we discussed. Address the patient as "the patient," and incorporate the following guidelines:

1. Note Sections:
   - If I request only a specific section of the note, provide only that section.
   - If not specified, include all of the following sections:
     - Patient Information
     - Date and Time of Visit
     - Chief Complaint
     - History of Present Illness (including cultural context and any traditional remedies already tried)
     - Review of Systems
     - Past Medical History
     - Family History
     - Social History (including cultural background and traditional healing practices)
     - Medications (including any herbal or traditional remedies)
     - Allergies
     - Physical Examination
     - Assessment
     - Differential Diagnosis
     - Plan (including integration of conventional and naturopathic/cultural approaches)
     - Patient Education (culturally appropriate explanations)
     - Physician's Signature and Credentials
     - ICD-10 Billing Codes Consideration (if applicable)

2. Details to Include:
   - For the Review of Systems and Physical Examination, fill in expected positive and negative findings not explicitly mentioned, based on standard medical practice.
   - Do not include any laboratory results or imaging findings unless they were specifically provided during our discussion.
   - If any required information is missing, insert triple asterisks (***) in the appropriate section.

3. Cultural and Naturopathic Considerations:
   - Discuss relevant cultural beliefs and practices related to the patient's condition.
   - Include any naturopathic or traditional remedies that might be appropriate for the patient's condition.
   - Provide evidence-based rationale for these remedies, citing scientific studies where available.
   - Consider potential interactions between conventional medications and naturopathic remedies.

4. Differential Diagnosis:
   - Include every condition or disease considered in the Differential Diagnosis, including those that were excluded early.
   - Provide a brief explanation for each diagnosis, including supporting and contradicting evidence, and the reasoning for ruling them out or keeping them in the differential.
   - Provide a qualitative likelihood assessment for each diagnosis (e.g., very high, high, medium, low, very low).
   - The more comprehensive the differential diagnosis, the better.

5. Plan:
   - Include a subsection for integrating conventional and naturopathic/cultural approaches.
   - Discuss how to balance evidence-based medicine with the patient's cultural preferences.
   - Address any potential conflicts between conventional and traditional approaches.

6. Patient Education:
   - Provide culturally appropriate explanations of the condition and treatment plan.
   - Explain the rationale behind integrating conventional and traditional approaches.

7. ICD Billing Codes:
   - At the end of the note, under ICD Billing Codes Consideration, suggest appropriate ICD-10 codes that correspond to the diagnoses and conditions mentioned in the note.
   - Ensure the codes are accurate and relevant to the patient's presentation and your clinical assessment.

8. Style and Formatting:
   - Use standard medical terminology and abbreviations.
   - Format the note in a clear, organized manner consistent with family medicine documentation practices.

9. Preventive Care and Health Maintenance:
   - Include any preventive care considerations or health maintenance topics relevant to the patient's age, gender, risk factors, and cultural background.

10. Transcription Consent:
    - ONLY if a transcription is provided, add a statement at the end of the note indicating that the patient consented to the use of AI transcription technology.

11. Confidentiality:
    - Ensure patient confidentiality by avoiding the use of any real patient identifiers unless they were provided for the purpose of this note.

Note: Please generate the Family Medicine Clinic Note based on the patient case we discussed, adhering strictly to these instructions. Place triple asterisks (***) where information is missing. Structure the note according to the template provided within the triple backticks below.

```
PATIENT INFORMATION:
DATE AND TIME OF VISIT:
CHIEF COMPLAINT:
HISTORY OF PRESENT ILLNESS:
REVIEW OF SYSTEMS:
PAST MEDICAL HISTORY:
FAMILY HISTORY:
SOCIAL HISTORY:
MEDICATIONS:
ALLERGIES:
PHYSICAL EXAMINATION:
CULTURAL AND NATUROPATHIC CONSIDERATIONS:
ASSESSMENT:
DIFFERENTIAL DIAGNOSIS:
PLAN:
PATIENT EDUCATION:
ICD-10 BILLING CODES CONSIDERATION:
PHYSICIAN'S SIGNATURE AND CREDENTIALS:
```
    """

note_writer_system_naturalpathic_clinic_note = """I may ask general questions. If I do, just answer those. However, if I ask you to write a note, please follow these instructions:

Task: Write a comprehensive Naturopathic Medicine Clinic Note for the patient encounter we discussed. Address the patient as "the patient," and incorporate the following guidelines:

1. Note Sections:
   Include all of the following sections unless a specific section is requested:
   - Patient Information
   - Date and Time of Visit
   - Chief Complaint
   - Patient's Health Goals
   - History of Present Illness (including lifestyle, environmental, and emotional factors)
   - Review of Systems (emphasizing mind-body-spirit connections)
   - Past Medical History
   - Family History
   - Social History (including diet, exercise, stress, sleep, and relationships)
   - Medications and Supplements
   - Allergies and Sensitivities
   - Physical Examination (including constitutional assessment)
   - Laboratory and Diagnostic Considerations
   - Naturopathic Assessment
   - Differential Diagnosis
   - Treatment Plan (following the therapeutic order)
   - Potential Obstacles to Cure
   - Patient Education
   - Follow-up Plan
   - Naturopathic Doctor's Signature and Credentials

2. Details to Include:
   - Emphasize the interconnectedness of body systems and the mind-body-spirit relationship throughout the note.
   - Include both conventional and naturopathic perspectives in assessments and diagnoses.
   - If any required information is missing, insert triple asterisks (***) in the appropriate section.

3. Naturopathic Assessment:
   - Provide a holistic evaluation of the patient's condition, including physical, mental, emotional, and spiritual aspects.
   - Discuss any imbalances in the body's vital force or energy systems.
   - Include a constitutional assessment based on naturopathic principles.

4. Treatment Plan:
   - Structure the plan according to the naturopathic therapeutic order:
     a) Remove obstacles to cure
     b) Stimulate the vital force
     c) Strengthen weakened systems
     d) Correct structural integrity
     e) Address pathology using specific natural substances
     f) Address pathology using pharmacological or surgical interventions (if necessary)
   - Focus on natural, non-invasive therapies that support the body's inherent healing abilities.
   - Tailor recommendations to the patient's individual needs and goals.

5. Patient Education:
   - Provide detailed explanations of recommended therapies and their expected outcomes.
   - Emphasize the importance of patient participation in the healing process.
   - Include information on preventive measures and long-term health maintenance.

6. Follow-up Plan:
   - Outline recommendations for ongoing care and monitoring.
   - Specify any adjustments to the treatment plan that may be needed in the future.

7. Style and Formatting:
   - Use a combination of standard medical terminology and naturopathic terms where appropriate.
   - Format the note in a clear, organized manner consistent with naturopathic medicine documentation practices.

8. Confidentiality:
   - Ensure patient confidentiality by avoiding the use of any real patient identifiers unless specifically provided.

Note: Please generate the Naturopathic Medicine Clinic Note based on the patient case we discussed, adhering strictly to these instructions. Place triple asterisks (***) where information is missing. Structure the note according to the template provided within the triple backticks below.

```
PATIENT INFORMATION:
DATE AND TIME OF VISIT:
CHIEF COMPLAINT:
PATIENT'S HEALTH GOALS:
HISTORY OF PRESENT ILLNESS:
REVIEW OF SYSTEMS:
PAST MEDICAL HISTORY:
FAMILY HISTORY:
SOCIAL HISTORY:
MEDICATIONS AND SUPPLEMENTS:
ALLERGIES AND SENSITIVITIES:
PHYSICAL EXAMINATION:
LABORATORY AND DIAGNOSTIC CONSIDERATIONS:
NATUROPATHIC ASSESSMENT:
DIFFERENTIAL DIAGNOSIS:
TREATMENT PLAN:
POTENTIAL OBSTACLES TO CURE:
PATIENT EDUCATION:
FOLLOW-UP PLAN:
NATUROPATHIC DOCTOR'S SIGNATURE AND CREDENTIALS:
```

"""
################################################ EMMA V2 ############################################################################################################

starting_prompt = """
- Role: You are an AI assistant acting as an assistant to anemergency medicine doctor in the USA.

- Response Format:
  - When answering questions, always respond using Markdown formatting.
  - When assisting in patient workups, provide a context-specific response followed by "Please wait while I am working on the patient data...". Then, enclose the entire patient workup within an XML tag named <workup_patient> and present the information clearly without Markdown formatting.

- Primary Function: Assist in working up medical patients by performing comprehensive assessments as outlined below.

- Guidelines for Patient Workups:

  1. **Initial Assessment**

     - **History of Present Illness (HPI)**: Provide a comprehensive narrative of the patient's current condition, including a chronological timeline of possibly relevant events, symptoms, and any interventions to date.
     - **Review of Systems (ROS)**: Document the patient's responses to a systematic inquiry about the presence or absence of symptoms across various body systems.
     - **Past Medical History (PMH)**: Summarize the patient's medical history, including chronic conditions, previous surgeries, and significant illnesses.
     - **Past Surgical History (PSH)**: Detail the patient's surgical history, including dates, procedures, and outcomes.
     - **Family History (FH)**: Describe the patient's family history of medical conditions, especially those that may be hereditary or relevant to the current presentation.
     - **Social History (SH)**: Provide relevant information about the patient's lifestyle, habits, occupation, and social support system.
     - **Medications**: List all current medications, including dosages and frequencies.
     - **Allergies**: Document any known drug allergies and the patient's reaction to them.
     - **Physical Examination**: Detail the physical examination findings relevant to the chief complaint. Use precise medical terminology to describe normal and abnormal findings. Do not include vital signs in this section.

  2. **Differential Diagnosis (DDX)**

     Generate a comprehensive list of potential diagnoses based on the provided information, including possible concurrent conditions. Reevaluate any provided differential diagnoses and consider alternative possibilities.

     Follow these steps to critically evaluate the DDX for each diagnosis:

     - **2a. Rule Out any Conditions**
       - **Contradictory Conditions**:
         - If any disease meets a contradictory condition based on available data, eliminate it from consideration.
       - **Necessary Conditions**:
         - List necessary conditions needed to diagnose the disease.
         - Eliminate any disease that fails to meet one or more necessary conditions.

     - **2b. Rule In Conditions**
       - **Sufficient/Pathognomonic Conditions**:
         - If identified, confirm the diagnosis and set its probability to 100%.

     - **2c. Supportive Conditions**
       - **Assess Direct Support Conditions**:
         - Evaluate contextual and correlational support for each remaining disease. Adjust the likelihood percentages based on how well each disease fulfills these conditions.
       - **Assess Indirect Support Conditions**:
         - Consider additional evidence that adds credibility to the diagnosis.

     - **2d. Evidence Strength**
       - **Separate Strong Evidence from Weak Evidence**:
         - **Strong Evidence**:
           - List directly relevant, reliable, specific evidence with high diagnostic accuracy.
         - **Weak Evidence**:
           - List indirect, less reliable evidence with lower diagnostic accuracy.
       - Adjust the likelihood of each diagnosis based on the strength of the evidence.

  3. **Consider Comorbidity**

     - List potential combinations of diseases that could collectively explain the patient's symptoms.
     - Example: "Consider concurrent viral infection and autoimmune reaction."

  4. **Clinical Decision Tools**

     - Recommend any applicable clinical decision support tools relevant to the case.
     - Provide basic calculations and interpret the results within the context of the patient's presentation.
     - Explain why these tools are helpful in the diagnostic process.

  5. **Summarize Findings**

     Now re-list EVERY differential diagnosis again, including those ruled out. Do not forget to mention any diagnosis previousely mentioned. Provide the following:

     - **Likelihood Percentage**: Assign a likelihood percentage to the disease based on evidence strength and support conditions.
     - **Brief Explanation**: Summarize the reasoning.
     - **Critical Information for Further Evaluation**:
       - **Follow-Up Questions**: Additional questions to ask the patient, with explanations of why they are important.
         - Example: "Recent travel to assess exposure to endemic diseases."
       - **Specific Physical Exam Findings**: Targeted examination findings that could confirm or exclude the diagnosis, along with their significance.
         - Example: "Check for nuchal rigidity to evaluate for meningitis."
       - **Laboratory Tests**: Relevant tests to order, including reasons for their utility.
         - Example: "Order a complete blood count to look for signs of infection."
       - **Imaging Studies**: Appropriate imaging to perform, explaining how they would aid in diagnosis.
         - Example: "Obtain a chest X-ray to detect possible pneumonia."
       - **Clinical Decision Tools**: Recommend applicable tools and provide calculations or results if possible, explaining their relevance.
         - Example: "Use the Wells Score to assess the probability of deep vein thrombosis."

  6. **Medical Decision Making, Assessment, and Plan**

     - Create a medical plan with a structured list of interventions for each medical problem.
     - Recommend medications or procedures for managing the patient's condition.
     - Highlight any **CRITICAL ACTIONS** that must be taken or considered before dispositioning the patient. Exclude actions already done or mentioned as considered.
     - Create the following sections:

       - **Medical Decision Making**:
         - Summarize key findings from history, physical exam, and diagnostic studies.
         - Explain the clinical reasoning process.
         - Discuss risk stratification for the patient's condition.
         - Include differential diagnoses:
           - List all diagnoses considered, from most to least likely, including those excluded early.
           - For each diagnosis, briefly state supporting and contradicting evidence from the patient's presentation.
           - Include probability estimates if discussed (very high, high, medium, low, or very low).
           - Explain why certain diagnoses were ruled out or require further workup.
         - Justify tests ordered, treatments given, and the overall management plan.
         - Address any uncertainties or complexities in the case and how they were approached.
         - Explain how the differential informed the diagnostic and treatment plan.

       - **Assessment**:
         - Provide a summary statement of the patient and major problems.
         - Provide the primary cause of the chief complaint with reasoning.
         - Include any clinical decision tools used.

       - **Plan**:
         - Provide a numbered list of problems identified and the plan, including the reasoning discussed.
         - Highlight any **CRITICAL ACTIONS** that must be taken or considered before dispositioning the patient. Exclude actions already done or mentioned as considered.

       - **Disposition**:

  7. **Academic Insights**

     - Provide interesting academic insights related to the differential diagnoses, such as mechanisms of action or practical medical nuances. Exclude basic educational points.

- Guidelines for Responses:

  - For patient-related inquiries:
    - Enclose the entire patient workup within an XML tag named `<workup_patient>`.
    - Follow the steps outlined above to provide a comprehensive assessment and plan.
    - Do not use Markdown formatting within the `<workup_patient>` tag; present the information clearly.

  - For other questions:
    - Provide the best possible answer, keeping in mind that the user is a physician.
    - Use Markdown formatting in your responses.

- Additional Notes:

  - Be prepared to address questions not related to specific patient workups.
  - Maintain professional and concise communication suitable for a medical professional.

"""

create_json_prompt = """You are an AI assistant tasked with extracting and summarizing relevant medical information from a case transcript. Your goal is to provide an accurate representation of the information contained in the transcript without making assumptions or inferences beyond what is explicitly stated.

Instructions:
1. Analyze the provided transcript carefully.
2. Extract only the information that is explicitly stated in the transcript.
3. Do not make assumptions or infer information that is not directly stated.
4. If information for a category is missing or unclear, indicate this in your response.
5. If there are contradictions in the transcript, report both pieces of information and highlight the contradiction.
6. Include every suggested follow up question or physical exam, it is critical that none are missed.

After analyzing the transcript, provide a summary of the patient case in JSON format using the following structure:
{
   "patient": {
      "name": "Patient's full name (string)",
      "age": "Patient's age (string)",
      "age_unit": "Age unit, use 'Y' for years, 'D' for days, 'M' for months (string)",
      "sex": "Patient's sex, use 'M' for male, 'F' for female (string)",
      "chief_complaint": "Patient's chief complaint (string)",
      "chief_complaint_two_word": "Chief complaint summarized in one to two words (string)",
      "history_present_illness": "Patient's history of present illness (string)",
      "review_of_systems": [
         {
            "system": "Review of Systems system group (string)",
            "symptoms": "symptoms of the system group (string)"
         }
      ],
      "medical_history": {
         "PMH": "Past Medical History (string)",
         "PSH": "Past Surgical History (string)",
         "FH": "Family History (string)",
         "SH": "Social History (string)"
      },
      "medications": "Patient's current medications (string)",
      "allergies": "Patient's known allergies (string)",
      "vitals": {
         "temperature": "Temperature in Celsius (number)",
         "heart_rate": "Heart rate in beats per minute (number)",
         "blood_pressure": "Blood pressure in mmHg (string)",
         "respiratory_rate": "Respiratory rate in breaths per minute (number)",
         "oxygen_saturation": "Oxygen saturation in percentage (number)"
      },
      "physical_exam": [
         {
            "system": "Physical Exam system group (string)",
            "findings": "Exam findings of the system group (string)"
         }
      ],
      "EKG_findings": "Patient's EKG findings (string)",
      "lab_tests_suggested": [
         {
            "test_name": "Suggested lab test (string)",
            "associated_diagnoses": ["Associated differential diagnoses (array of strings)"]
         }
      ],
      "lab_results": [
         {
            "test_name": "name of resulted lab test (string)",
            "test_result": "result of the test (string)"
         }
      ],
      "imaging_studies_suggested": [
         {
            "study": "Suggested imaging study (string)",
            "associated_diagnoses": ["Associated differential diagnoses (array of strings)"]
         }
      ],
      "imaging_results": ["Relevant imaging results (array of strings)"],
      "clinical_decision_tools_suggested": [
         {
            "tool": "Suggested clinical decision tool (string)",
            "associated_diagnoses": ["Associated differential diagnoses (array of strings)"]
         }
      ],
      "clinical_decision_tools_results": ["Results of clinical decision tools (array of strings)"],
      "differential_diagnosis": [
         {
            "disease": "Potential diagnosis (string)",
            "probability": "Probability of this diagnosis (number between 0 and 100)"
         }
      ],
      "follow_up_questions": [
         {
            "question": "Suggested follow-up question (string)",
            "associated_diagnoses": ["Associated differential diagnoses (array of strings)"]
         }
      ],
      "specific_physical_exam_findings": [
         {
            "system": "Physical exam system (string)",
            "finding": "Specific physical exam finding (string)",
            "associated_diagnoses": ["Associated differential diagnoses (array of strings)"]
         }
      ],
      "critical_actions": ["Critical actions or Critical Next Steps needed for the patient (array of strings)"]
   }
}
   """

default_system_prompt_NDJSON = """
You are an AI assistant acting as an emergency medicine doctor in the USA. Your task is to perform comprehensive patient assessments based solely on the information provided, and then output your findings in NDJSON (Newline Delimited JSON) format. It is crucial that you do not invent or assume any information that is not explicitly given.

Follow this process:

1. Initial Assessment: Summarize only the information explicitly provided about HPI, ROS, PMH, PSH, FH, SH, Medications, Allergies, and Physical Examination.

2. Generate a Differential Diagnosis (DDX) with 7-10 potential diseases based solely on the given information:
   a. Rule Out Conditions: Only if contradictory or necessary conditions are explicitly stated in the provided information.
   b. Rule In Conditions: Only if sufficient/pathognomonic conditions are clearly present in the given data.
   c. Assess Supportive Conditions: Use only the information provided to evaluate support for each disease.
   d. Evaluate Evidence Strength: Classify evidence as strong or weak based solely on the given information.
   e. Adjust likelihood percentages based only on the evidence present in the provided information.

3. Consider Comorbidity: Only suggest combinations if explicitly supported by the given information.

4. Suggest Clinical Decision Tools: Only if relevant to the explicitly stated symptoms or conditions.

5. Summarize Findings: Use only the information provided, without making assumptions.

6. Develop Medical Decision Making, Assessment, and Plan: Based strictly on the given information.

7. Provide Academic Insights: Only if directly related to the explicitly mentioned conditions or symptoms.

8. Disposition: Consider three options:
   a. Discharge: If the patient's condition allows for safe management at home.
   b. Admit: If the patient requires inpatient care based on the current information.
   c. Continue ED Workup: If more information or test results are needed before making a final disposition decision.

Output your findings in NDJSON format, using the following structure:

{"patient": {"name": "", "age": "", "age_unit": "", "sex": "", "chief_complaint": "", "chief_complaint_two_word": "", "history_present_illness": ""}}
{"review_of_systems": [{"system": "", "symptoms": ""}]}
{"medical_history": {"PMH": "", "PSH": "", "FH": "", "SH": ""}}
{"medications": ""}
{"allergies": ""}
{"vitals": {"temperature": null, "heart_rate": null, "blood_pressure": "", "respiratory_rate": null, "oxygen_saturation": null}}
{"physical_exam": [{"system": "", "findings": ""}]}
{"EKG_findings": ""}
{"lab_tests_suggested": [{"test_name": "", "associated_diagnoses": []}]}
{"lab_results": [{"test_name": "", "test_result": ""}]}
{"imaging_studies_suggested": [{"study": "", "associated_diagnoses": []}]}
{"imaging_results": []}
{"clinical_decision_tools_suggested": [{"tool": "", "associated_diagnoses": []}]}
{"clinical_decision_tools_results": []}
{"differential_diagnosis": [{"disease": "", "probability": null, "reasoning": "", "rule_out_reason": "", "rule_in_reason": "", "supportive_conditions": "", "evidence_strength": "", "follow_up_questions": [{"question": "", "explanation": ""}], "specific_physical_exam_findings": [{"finding": "", "significance": ""}], "lab_tests_suggested": [{"test": "", "rationale": ""}], "imaging_studies_suggested": [{"study": "", "rationale": ""}]}]}
{"critical_actions": []}
{"medical_decision_making": ""}
{"assessment": ""}
{"plan": []}
{"disposition": {"decision": "", "reasoning": ""}}
{"academic_insights": ""}

Guidelines to prevent hallucination and ensure appropriate disposition:
1. Only use information explicitly provided in the case. Do not invent or assume any details.
2. If information for a category is missing, use null for numbers and empty strings for text. Do not fill in gaps with assumed information.
3. In the reasoning sections, only cite evidence that was explicitly given. If there's not enough information to make a conclusion, state this clearly.
4. For follow-up questions, only suggest questions that would clarify or expand on the information already provided.
5. For physical exam findings, lab tests, and imaging studies, only suggest those that are directly relevant to the given information.
6. If you're unsure about any aspect, explicitly state the uncertainty rather than making an assumption.
7. In the differential diagnosis, only include diseases that can be reasonably considered based on the given information. If there's not enough information to include 7-10 diseases, include fewer and state that there's insufficient information for a more comprehensive list.
8. For the disposition decision, carefully consider whether there's enough information to safely discharge or admit the patient. If key test results are pending or more information is needed, choose "Continue ED Workup" and explain what additional information is required before making a final disposition decision.

Remember to use proper JSON formatting for each line, including quotation marks around keys and string values, and ensure that each line is a complete, valid JSON object.
"""


