# Walk_in_Clinic_Simulation.py
#
# Description: Calculates or displays arrival time, departure time,
#              total wait time, and average wait time of patients
#              waiting in a clinic to see the doctor.
#
# Peter Tran
#
# February 2017

# Print the introduction.
print("Walk in Clinic Simulation - Start")

# Ask for user input of arrival times for the patients.
arrive = input("Please, enter arrival time of patients: \n")

#Convert arrival times into a list.
arrive = arrive.split()

# Create a new list, turn arrival times into integers. Then append these
# integers into this new list.
arriveTime = []
for time in arrive :
    arriveTime.append(int(time))

# Assign variable timer to keep track of time. Time begins when the first patient enters.
timer = arriveTime[0]
# Assign variable for the waitlist. Patients are in the waitlist until they see doctor.
wait = 0
# Assign variable to keep track of index.
index = 0
# Assign variable for the departure time.
leaving = 0
# Assign variable to keep track of waiting time.
waitTime = 0
# This list is for storing all leaving times. 
leavingTime=[]

# While the time is <= the final arrival time, or while the time is <= the departure time,
# or while the wait list is occupied, run the following.
while ((timer <= arriveTime[-1]) or (timer <= leaving) or wait != 0) :
    
    # If index < length(arrivetime) and if the time is the same as the time a patient arrives,
    # Print that a patient has arrived at this time.
    if index < len(arriveTime) and timer == arriveTime[index] :
        print("Patient arriving at clinic at %d" %(timer))
        
        # If the wait list is empty, observe these conditions:
        if wait == 0 :

            # If the departure time is >= the time, add patient to the wait list.
            if leaving >= timer :
                wait += 1

            # Otherwise, if the doctor is free, the patient can see the doctor.
            else :
                leaving = timer + 5

        # If the wait list is occupied, add to the wait list. 
        else:
            wait += 1

        # Increase the index by 1.    
        index += 1

    # When the timer reaches the time when a patient is to leave, print that they are leaving,
    # and append their departure time into the departure list
    if timer == leaving :
        print("Patient departing at clinic at %d" %(timer))
        leavingTime.append(timer)

        # If they were on the wait list, take them off.
        if wait != 0 :
            wait -= 1
            leaving = timer + 5
            
    # To keep track of time. Each iteration, the time moves up by one.  
    timer += 1
    
# Assign index back to 0 for the next while loop.
index = 0

# This while loop is to calculate the total wait time of all the patients.
while index < len(arriveTime) :

    # If a patient had to wait (that is, if the time between departure and arrival is greater than 5),
    # add to the total wait time.
    if leavingTime[index] - arriveTime[index] > 5 :
        waitTime += ((leavingTime[index] - arriveTime[index]) - 5)

    # Progress through the indexes of both lists.
    index += 1

# Print the Simulation result.
print("\nSimulation result:")

# Print the total number of patients.
print("Total number of patients: %s" %(len(arriveTime)))

# This is the total wait time.     
print("Total wait time: %d" %(waitTime))

# This is the average wait time.
print("Average wait time per patient: %g" %(waitTime / len(arriveTime)))

# Indicates the end of the simulation.
print("Walk in Clinic Simulation - End")
