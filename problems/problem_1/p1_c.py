def stable_matching_1c(file_path) -> dict:
    number_of_entities = 0
    doctor_preferences = []
    hospital_preferences = []

    # Read the file and store doctors' and hospitals' preferences
    with open(file_path, "r") as file:
        number_of_entities = int(file.readline())
        # Capture doctor preferences
        for _ in range(number_of_entities):
            preferences = list(map(int, file.readline().split()))
            doctor_preferences.append(preferences)

        # Capture hospital preferences
        for _ in range(number_of_entities):
            preferences = list(map(int, file.readline().split()))
            hospital_preferences.append(preferences)

    matches = {}
    unmatched_doctors = set()

    # Create a dictionary to hold hospital rankings based on doctor preferences
    hospital_rankings = {}
    for index in range(number_of_entities):
        hospital_rankings[index] = {}
        for rank, doctor in enumerate(hospital_preferences[index]):
            hospital_rankings[index][doctor] = rank

    # List to keep track of the next hospital each doctor will propose to
    next_hospital_proposals = [0] * number_of_entities

    # List of available doctors
    available_doctors = list(range(number_of_entities))

    # Continue until there are no available doctors
    while available_doctors:
        current_doctor = available_doctors.pop(0)  # Get the next free doctor
        current_hospital = doctor_preferences[current_doctor][next_hospital_proposals[current_doctor]]
        next_hospital_proposals[current_doctor] += 1  # Move to the next hospital

        # If the hospital is currently unmatched
        if current_hospital not in matches:
            matches[current_hospital] = current_doctor  # Match the hospital to this doctor
            unmatched_doctors.add(current_doctor)
        else:
            existing_doctor = matches[current_hospital]  # Get the doctor currently matched to this hospital
            
            # Check if the hospital prefers the new doctor over the existing one
            if hospital_rankings[current_hospital][current_doctor] < hospital_rankings[current_hospital][existing_doctor]:
                matches[current_hospital] = current_doctor  # Update match to the new doctor
                unmatched_doctors.add(current_doctor)
                unmatched_doctors.remove(existing_doctor)  # The previous doctor is now unmatched
                available_doctors.append(existing_doctor)  # Make the replaced doctor available again
            else:
                available_doctors.append(current_doctor)  # Doctor remains unmatched

    # Create a result dictionary mapping doctors to hospitals
    final_matches = {doctor: hospital for hospital, doctor in matches.items()}

    return final_matches
