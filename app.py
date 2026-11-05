import streamlit as st
from generator import generate_hospital_management_answer

st.set_page_config(page_title="AI for Hospital Management", page_icon="🏥", layout="wide")
st.title("🏥 AI for Hospital Management")
st.caption("An AI assistant for learning about hospital administration and healthcare operations.")

with st.sidebar:
    st.header("Response settings")
    knowledge_level = st.selectbox("Your role / knowledge level", [
        "Student / Beginner", "Hospital Administration Student",
        "Healthcare Professional", "Hospital Manager / Administrator", "Researcher"
    ])
    response_style = st.selectbox("Response style", [
        "Clear and practical", "Simple explanation", "Detailed analysis",
        "Step-by-step workflow", "Professional report"
    ])
    include_examples = st.toggle("Include practical examples", True)
    include_metrics = st.toggle("Include relevant KPIs", True)
    include_checklist = st.toggle("Include an action checklist", True)

topic = st.selectbox("Hospital management area", [
    "General hospital management", "Patient registration and admission",
    "Appointment and OPD management", "Emergency department workflow",
    "Bed and ward management", "Patient flow and discharge planning",
    "Hospital staff and duty scheduling", "Pharmacy and inventory management",
    "Medical equipment and maintenance", "Hospital billing and revenue cycle",
    "Quality assurance and patient safety", "Infection prevention and control",
    "Hospital information systems (HIS / HMIS)", "Healthcare data and dashboards",
    "Hospital waste management", "Accreditation and compliance", "Other / general question"
])

question = st.text_area(
    "Enter your question or describe the management problem",
    placeholder="Example: How can a 200-bed hospital reduce admission delays and improve bed utilisation?",
    height=130
)
extra_context = st.text_area(
    "Optional context",
    placeholder="Example: 150-bed multispecialty hospital; high OPD volume; limited nursing staff.",
    height=80
)

if st.button("Generate Management Guidance", type="primary", use_container_width=True):
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Preparing management guidance..."):
            try:
                result = generate_hospital_management_answer(
                    question=question.strip(), topic=topic,
                    knowledge_level=knowledge_level, response_style=response_style,
                    include_examples=include_examples, include_metrics=include_metrics,
                    include_checklist=include_checklist, extra_context=extra_context.strip()
                )
                st.success("Guidance generated.")
                st.header("Management Guidance")
                st.write(result.overview)

                st.subheader("Key Concepts")
                for item in result.key_concepts:
                    st.markdown(f"- {item}")

                st.subheader("Recommended Workflow")
                for i, step in enumerate(result.workflow_steps, 1):
                    st.markdown(f"**{i}. {step.title}**")
                    st.write(step.description)
                    if step.responsible_role:
                        st.caption(f"Suggested responsibility: {step.responsible_role}")

                if result.practical_example:
                    st.subheader("Practical Example")
                    st.write(result.practical_example)

                if result.relevant_kpis:
                    st.subheader("Suggested KPIs")
                    for kpi in result.relevant_kpis:
                        st.markdown(f"- **{kpi.name}:** {kpi.description}")
                        if kpi.calculation:
                            st.caption(f"Calculation: {kpi.calculation}")

                if result.action_checklist:
                    st.subheader("Action Checklist")
                    for item in result.action_checklist:
                        st.markdown(f"- [ ] {item}")

                if result.risks_and_safeguards:
                    st.subheader("Risks and Safeguards")
                    for item in result.risks_and_safeguards:
                        st.markdown(f"- {item}")

                if result.assumptions_or_missing_information:
                    st.subheader("Assumptions / Information to Confirm")
                    for item in result.assumptions_or_missing_information:
                        st.markdown(f"- {item}")

                if result.further_considerations:
                    st.subheader("Further Considerations")
                    for item in result.further_considerations:
                        st.markdown(f"- {item}")

                st.divider()
                st.caption("General educational and operational guidance only. Not a substitute for clinical judgement, legal advice, local regulations, or hospital policies. Do not enter identifiable patient information.")
            except Exception:
                st.error("The response could not be generated. Check your API key, model configuration, and deployment logs.")
                st.exception(Exception("See the deployment logs for the underlying error."))

st.divider()
st.caption("Prototype for learning and demonstration. Not a production Hospital Information System.")
