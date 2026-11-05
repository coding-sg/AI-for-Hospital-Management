# AI for Hospital Management
https://ai-for-hospital-management-fpaqu3jywknjhnaehtug5i.streamlit.app/

An educational AI assistant built with Streamlit, LangChain, and Google Gemini.
It helps users explore hospital administration and healthcare operations.

## Features
- OPD/IPD, registration, appointments, emergency workflows, beds and discharge planning
- Staffing, pharmacy and inventory, equipment maintenance, billing
- Quality, patient safety, infection prevention, HMIS, dashboards and accreditation
- Adjustable knowledge level and response style
- Structured workflows, illustrative examples, KPIs and action checklists
- Risks, safeguards, assumptions and further considerations

## Files
- `app.py` – Streamlit interface
- `generator.py` – Gemini / LangChain integration
- `prompts.py` – Assistant instructions and prompt
- `schemas.py` – Structured response models
- `requirements.txt` – Dependencies
- `.env.example` – Example environment variables

## Run locally
1. Create and activate a Python virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file based on `.env.example`.
4. Add your Gemini API key to `.env`.
5. Run: `streamlit run app.py`

## Responsible-use notice
This is a learning and demonstration prototype, not a production Hospital
Information System (HIS/HMIS). It does not connect to hospital records. Do not
use it for autonomous clinical decisions, diagnosis, treatment, triage, discharge,
staff allocation, billing, or regulatory certification. Operational recommendations
must be reviewed by authorised hospital personnel and checked against local
policies and current regulations.

Do not enter identifiable patient information or confidential hospital data.
Use synthetic or properly de-identified examples only.

## Acknowledgements

This project was developed as part of the hands-on training and learning experience at **Innomatics Research Labs**.

I would like to express my sincere gratitude to the trainers and mentors who guided me throughout the workshop, helped me understand the concepts, and provided practical exposure to AI application development using Python, LangChain and Streamlit.

Their guidance and support contributed to the development of this project.
