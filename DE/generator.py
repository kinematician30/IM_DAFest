import csv
import json
import logging
import random
from random import randint

from faker import Faker
from faker.providers import DynamicProvider

# Configure logging
logging.basicConfig(filename='student_data_generation.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# to give the same state for each instance spin.
Faker.seed(1000)
random.seed(1000)

# Faker instance
fake = Faker()

# Create Dynamic (Customized) providers for each of the elements you provided
gender_provider = DynamicProvider(
    provider_name="gender",
    elements=["Male", "Female"]
)

state_provider = DynamicProvider(
    provider_name="state",
    elements=["Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno",
              "Cross River", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "Gombe", "Imo", "Jigawa",
              "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger",
              "Ogun", "Ondo", "Osun", "Oyo", "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe",
              "Zamfara", "FCT"]
)

education_provider = DynamicProvider(
    provider_name="parent_education",
    elements=["No formal education", "Primary school", "Secondary school", "University", "Postgraduate(Masters,PhD)"]
)

income_provider = DynamicProvider(
    provider_name="household_income",
    elements=["Low income", "Middle income", "High income"]
)

study_duration_provider = DynamicProvider(
    provider_name="study_duration",
    elements=["Less than 1 hour", "1-2 hours", "2-4 hours", "More than 4 hours"]
)

study_frequency_provider = DynamicProvider(
    provider_name="study_frequency",
    elements=["Every day", "4-6 times a week", "2-3 times a week", "Once a week", "Only before exams", "Never"]
)

learning_style_provider = DynamicProvider(
    provider_name="learning_style",
    elements=["Reading notes", "Watching videos", "Listening to lectures", "Group discussions", "Hands-on practice"]
)

study_resources_provider = DynamicProvider(
    provider_name="study_resources",
    elements=["Textbooks", "Online materials", "Past questions", "Videos", "Tutor"]
)

past_exam_practice_provider = DynamicProvider(
    provider_name="past_exam_practice",
    elements=["Always", "Often", "Sometimes", "Rarely", "Never"]
)

study_space_provider = DynamicProvider(
    provider_name="study_space",
    elements=["Yes", "No"]
)

attendance_provider = DynamicProvider(
    provider_name="attendance",
    elements=["Always", "Almost always", "Sometimes", "Rarely", "Never"]
)

study_impact_provider = DynamicProvider(
    provider_name="study_impact",
    elements=["Helps a lot", "Helps somewhat", "No impact", "Hinders somewhat", "Hinders a lot"]
)

teacher_support_provider = DynamicProvider(
    provider_name="teacher_support",
    elements=["Always", "Usually", "Sometimes", "Rarely", "Never"]
)

progress_monitoring_provider = DynamicProvider(
    provider_name="progress_monitoring",
    elements=["Always", "Often", "Sometimes", "Rarely", "Never"]
)

performance_provider = DynamicProvider(
    provider_name="performance",
    elements=["I performed better than expected", "I performed as expected", "I performed worse than expected"]
)

score_level_provider = DynamicProvider(
    provider_name="score_level",
    elements=["< 120", "120 - 200", "200 - 270", "> 270"]
)

# Add Customized Providers to the faker library
fake.add_provider(gender_provider)
fake.add_provider(state_provider)
fake.add_provider(education_provider)
fake.add_provider(income_provider)
fake.add_provider(study_duration_provider)
fake.add_provider(study_frequency_provider)
fake.add_provider(learning_style_provider)
fake.add_provider(study_resources_provider)
fake.add_provider(past_exam_practice_provider)
fake.add_provider(study_space_provider)
fake.add_provider(attendance_provider)
fake.add_provider(study_impact_provider)
fake.add_provider(teacher_support_provider)
fake.add_provider(progress_monitoring_provider)
fake.add_provider(performance_provider)
fake.add_provider(score_level_provider)

# logging info 1
msg_1 = "Added all dynamic providers"
print(msg_1)
logger.info(msg_1)


# Function to generate a specific number of student data records
def generate_student_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Timestamp": fake.date_time_this_year(),
            "ID": _ + 1,
            "Gender": fake.gender(),
            "State": fake.state(),
            "Parent Education Level": fake.parent_education(),
            "Household Income Level": fake.household_income(),
            "Study Duration": fake.study_duration(),
            "Study Frequency": fake.study_frequency(),
            "Learning Style": fake.learning_style(),
            "Study Resources": fake.study_resources(),
            "Past Exam Practice": fake.past_exam_practice(),
            "Study Space": fake.study_space(),
            "Attendance": fake.attendance(),
            "Study Impact by extracurricular activity": fake.study_impact(),
            "Teacher Support": fake.teacher_support(),
            "Progress Monitoring": fake.progress_monitoring(),
            "Performance": fake.performance(),
            "Score Level": fake.score_level()
        }
        data.append(record)
        logger.info(record)
    msg_2 = "all records successfully added to temp storage"
    logger.info(msg_2)
    return data


def generate_student_literacy_data(number_records):
    data = []
    record = {

    }
    pass


# Function to write data to CSV
def write_to_csv(data, filename):
    if data:
        keys = data[0].keys()
        with open(filename, 'w', newline='') as csvfile:
            msg_3 = f"Opened {filename}"
            msg_4 = f"Saved to {filename}"
            print(msg_3)
            logger.info(msg_3)
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
            print(msg_4)
            logger.info(msg_4)


# Function to write data to JSON
def write_to_json(data, filename):
    with open(filename, 'w') as jsonfile:
        msg_3 = f"Opened {filename}"
        msg_4 = f"Saved to {filename}"
        print(msg_3)
        logger.info(msg_3)
        json.dump(data, jsonfile, default=str, indent=4)  # dump json data in json file
        print(msg_4)
        logger.info(msg_4)


# Execute student record generator.
n_rec = randint(5000, 5500)
student_data = generate_student_data(n_rec)

# Output to CSV and JSON
write_to_csv(student_data, filename='..\\Datasets\\student_data_new.csv')
write_to_json(student_data, filename='..\\Datasets\\student_data_new.json')

print(f"{n_rec} records written to 'student_data.csv' and 'student_data.json'.")
logger.info(f"{n_rec} records written to 'student_data.csv' and 'student_data.json'.")
