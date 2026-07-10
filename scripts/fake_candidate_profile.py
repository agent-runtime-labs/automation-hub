from mcp.server.fastmcp import FastMCP
from faker import Faker
import random

# Initialize the FastMCP Server
mcp = FastMCP("CandidateDataServer")
fake = Faker('en_US')

NURSING_SPECIALTIES = [
    "Emergency Room Nurse", "ICU Nurse", "Labor & Delivery Nurse", 
    "OR Nurse (Operating Room)", "Neonatal ICU (NICU) Nurse", "Pediatric Nurse"
]

SKILLS_MAP = {
    "Emergency Room Nurse": ["Emergency Care", "Trauma", "Triage", "IV Insertion", "Rapid Assessment"],
    "ICU Nurse": ["Critical Care", "Ventilator Management", "Hemodynamic Monitoring", "ACLS", "ECMO"],
    "Labor & Delivery Nurse": ["Fetal Monitoring", "Epidural Management", "Neonatal Resuscitation", "Postpartum Care"],
    "OR Nurse (Operating Room)": ["Scrubbing & Circulating", "Sterile Technique", "Surgical Assisting", "Patient Safety"],
    "Neonatal ICU (NICU) Nurse": ["Neonatal Care", "Intubation Assisting", "PALS", "Total Parenteral Nutrition"],
    "Pediatric Nurse": ["Pediatric Assessment", "Child Life Support", "Family-Centered Care", "Immunizations"]
}

CERTIFICATIONS_MAP = {
    "Emergency Room Nurse": ["BLS", "ACLS", "PALS", "TNCC"],
    "ICU Nurse": ["BLS", "ACLS", "CCRN"],
    "Labor & Delivery Nurse": ["BLS", "ACLS", "NRP"],
    "OR Nurse (Operating Room)": ["BLS", "ACLS", "CNOR"],
    "Neonatal ICU (NICU) Nurse": ["BLS", "NRP", "PALS"],
    "Pediatric Nurse": ["BLS", "PALS", "CPN"]
}

SHIFTS = ["Days", "Nights", "Rotating", "Flexible"]
AVAILABILITY_OPTIONS = ["Immediate", "2 Weeks Notice", "4 Weeks Notice", "Available Next Month"]

@mcp.tool()
def generate_candidates(count: int = 1) -> str:
    """
    Generates synthetic nursing candidate profiles in a standard plain-text format.
    
    Args:
        count: The number of candidate profiles to generate (default is 1).
    """
    profiles = []
    for _ in range(count):
        specialty = random.choice(NURSING_SPECIALTIES)
        experience_years = random.randint(2, 15)
        state = fake.state()
        city = fake.city()
        location = f"{city}, {state}"
        
        base_pay = random.randint(1800, 2500)
        exp_bonus = experience_years * random.randint(70, 120)
        expected_pay = f"${base_pay + exp_bonus:,}"
        
        skills = ", ".join(random.sample(SKILLS_MAP[specialty], k=3))
        certs = ", ".join(CERTIFICATIONS_MAP[specialty])
        
        profile_text = (
            "Candidate Profile\n"
            f"Name: {fake.name()}\n"
            f"Candidate ID: RN-{random.randint(1000, 9999)}\n"
            f"Specialty: {specialty}\n"
            f"Location: {location}\n"
            f"Experience: {experience_years} Years\n"
            f"Licenses: {state} RN (Active)\n"
            f"Certifications: {certs}\n"
            f"Travel Assignments: {random.randint(0, 8)}\n"
            f"Availability: {random.choice(AVAILABILITY_OPTIONS)}\n"
            f"Preferred Shift: {random.choice(SHIFTS)}\n"
            f"Expected Weekly Pay: {expected_pay}\n"
            f"Skills: {skills}\n"
            f"Professional Summary: {specialty} experienced in high-volume settings with over {experience_years} years of background, focusing on high-quality patient outcomes and strong team collaboration."
        )
        profiles.append(profile_text)
        
    # Join multiple profiles with a separator if the agent requests more than 1
    return "\n\n---\n\n".join(profiles)

if __name__ == "__main__":
    mcp.run()