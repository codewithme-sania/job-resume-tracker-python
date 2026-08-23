jobs = []


# Add Job
def add_job():
    print("\n========== ADD JOB ==========")

    job_id = len(jobs) + 1
    company = input("Enter company name: ")
    role = input("Enter job role: ")
    status = input("Enter application status (Applied/Interview/Rejected/Selected): ")
    interview_date = input("Enter interview date (or type 'Not scheduled'): ")

    job = {
        "id": job_id,
        "company": company,
        "role": role,
        "status": status,
        "interview": interview_date
    }

    jobs.append(job)

    print("\nJob added successfully!")


# View Jobs
def view_jobs():
    print("\n========== ALL JOBS ==========")

    if len(jobs) == 0:
        print("No jobs found.")
        return

    for job in jobs:
        print("\nJob ID:", job["id"])
        print("Company:", job["company"])
        print("Role:", job["role"])
        print("Status:", job["status"])
        print("Interview Date:", job["interview"])


# Search Company
def search_company():
    print("\n========== SEARCH COMPANY ==========")

    company_name = input("Enter company name to search: ")

    found = False

    for job in jobs:
        if job["company"].lower() == company_name.lower():
            print("\nJob ID:", job["id"])
            print("Company:", job["company"])
            print("Role:", job["role"])
            print("Status:", job["status"])
            print("Interview Date:", job["interview"])

            found = True

    if not found:
        print("Company not found.")


# Update Application
def update_application():
    print("\n========== UPDATE APPLICATION ==========")

    if len(jobs) == 0:
        print("No jobs available.")
        return

    job_id = int(input("Enter Job ID to update: "))

    found = False

    for job in jobs:
        if job["id"] == job_id:

            print("\nCurrent Details:")
            print("Company:", job["company"])
            print("Role:", job["role"])
            print("Status:", job["status"])
            print("Interview Date:", job["interview"])

            new_status = input("\nEnter new application status: ")
            new_interview = input("Enter new interview date: ")

            job["status"] = new_status
            job["interview"] = new_interview

            print("\nApplication updated successfully!")

            found = True
            break

    if not found:
        print("Job ID not found.")


# Delete Application
def delete_application():
    print("\n========== DELETE APPLICATION ==========")

    if len(jobs) == 0:
        print("No jobs available.")
        return

    job_id = int(input("Enter Job ID to delete: "))

    found = False

    for job in jobs:
        if job["id"] == job_id:
            jobs.remove(job)

            print("\nApplication deleted successfully!")

            found = True
            break

    if not found:
        print("Job ID not found.")


# Show Applied Jobs
def show_applied_jobs():
    print("\n========== APPLIED JOBS ==========")

    found = False

    for job in jobs:
        if job["status"].lower() == "applied":

            print("\nJob ID:", job["id"])
            print("Company:", job["company"])
            print("Role:", job["role"])
            print("Status:", job["status"])
            print("Interview Date:", job["interview"])

            found = True

    if not found:
        print("No applied jobs found.")


# Show Interview Jobs
def show_interview_jobs():
    print("\n========== INTERVIEW JOBS ==========")

    found = False

    for job in jobs:
        if job["status"].lower() == "interview":

            print("\nJob ID:", job["id"])
            print("Company:", job["company"])
            print("Role:", job["role"])
            print("Status:", job["status"])
            print("Interview Date:", job["interview"])

            found = True

    if not found:
        print("No interview jobs found.")


# Main Menu
while True:

    print("\n==============================")
    print("      JOB & RESUME TRACKER")
    print("==============================")

    print("1. Add Job")
    print("2. View Jobs")
    print("3. Search Company")
    print("4. Update Application")
    print("5. Delete Application")
    print("6. Show Applied Jobs")
    print("7. Show Interview Jobs")
    print("8. Exit")

    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_job()

    elif choice == "2":
        view_jobs()

    elif choice == "3":
        search_company()

    elif choice == "4":
        update_application()

    elif choice == "5":
        delete_application()

    elif choice == "6":
        show_applied_jobs()

    elif choice == "7":
        show_interview_jobs()

    elif choice == "8":
        print("\nThank you for using Job & Resume Tracker!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 8.")