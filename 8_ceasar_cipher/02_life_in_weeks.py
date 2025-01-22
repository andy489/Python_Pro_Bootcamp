def life_in_weeks(curr_age):
    years_left = 90 - curr_age
    weeks_left = int((years_left * 364) / 7)

    print(f"You have {weeks_left} weeks left.")

life_in_weeks(20)