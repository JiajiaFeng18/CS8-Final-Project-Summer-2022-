from task_functions import *

#test for get_written_date()   
#assert get_written_date('01/02/2022') == 'January 2, 2022'
#assert get_written_date('01/12/1970') == 'January 12, 1970'
#assert get_written_date('04/14/2020') == 'April 14, 2020'
#assert get_written_date('06/19/2000') == 'June 19, 2000'
assert get_written_date(["01", "01", "1970"]) == "January 1, 1970"
assert get_written_date(["02", "03", "2000"]) == "February 3, 2000"
assert get_written_date(["10", "15", "2022"]) == "October 15, 2022"
assert get_written_date(["12", "31", "2021"]) == "December 31, 2021"
#-------------------------------------------------------------------------------------------

priority_scale = {
    1: "Lowest",
    2: "Low",
    3: "Medium",
    4: "High",
    5: "Highest"
}

#test for is_valid_name()
assert is_valid_name("He") == False
assert is_valid_name("Hello") == True
#test for is_valid_priority()
assert is_valid_priority(11, priority_scale) == False
assert is_valid_priority('11', priority_scale) == False
assert is_valid_priority('5', priority_scale) == True
#test for is_valid_date()
assert is_valid_month("01/01/1970") == True
assert is_valid_month("12/31/2021") == True
assert is_valid_month("21/01/1970") == False
assert is_valid_month("21/01/1970") == False
assert is_valid_day("02/03/2000") == True
assert is_valid_day("12/31/2021") == True
assert is_valid_day("02/33/2000") == False
assert is_valid_day("02/31/2021") == False
assert is_valid_day("02/1st/2021") == False
assert is_valid_day("14/1st/2021") == False
assert is_valid_year("12/31/2021") == True
assert is_valid_year("10/15/2022") == True
assert is_valid_year("12/31/2021") == True
assert is_valid_year("10/15/22") == False
assert is_valid_year("12/31/-21") == False
assert is_valid_date("March/31/2021") == False
assert is_valid_date("12/31/2021") == True
#test for is_valid_completion()
assert is_valid_completion("yes") == True
assert is_valid_completion("no") == True
assert is_valid_completion("haha") == False
#test for get_new_task()
assert get_new_task(['Book tickets', 'Verify dates', '3', '05/05/2022', 'no'], priority_scale) == {'name': 'Book tickets', 'info': 'Verify dates', 'priority': 3, 'duedate': '05/05/2022', 'done': 'no'}
assert get_new_task([42, "Go to Mount Doom and throw it in", "5", "03/25/3019", "yes"], priority_scale) == ("type", 42)
assert get_new_task([("hello", "world"), "Go to Mount Doom and throw it in", "5", "03/25/3019", "yes"], priority_scale) == ("type", ("hello", "world"))
assert get_new_task(["Destroy the ring", "Go to Mount Doom and throw it in", "5", 20, "yes"], priority_scale) == ("type", 20)
assert get_new_task(["Destroy the ring", "Go to Mount Doom and throw it in", "5", ("hello", "world"), "yes"], priority_scale) == ("type", ("hello", "world"))
#-------------------------------------------------------------------------------------------
#test for is_valid_index()
assert is_valid_index('0', ["Quizzes", 25.5]) == True
assert is_valid_index('1', ["Quizzes", 25.5]) == True
assert is_valid_index('2', ["Quizzes", 25.5]) == False
assert is_valid_index('2', ["Quizzes", 25.5], 1) == True # overwriting the default

all_tasks = [
    {
        "name": "Call XYZ",
        "info": "",
        "priority": 3,
        "duedate": '05/28/2022',
        "done": 'yes'
    },
    {
        "name": "Finish checkpoint 1 for CSW8",
        "info": "Submit to Gradescope",
        "priority": 5,
        "duedate": '06/02/2022',
        "done": 'no'
    },
    {
        "name": "Finish checkpoint 2 for CSW8",
        "info": "Implement the new functions",
        "priority": 5,
        "duedate": '06/05/2022',
        "done": 'no'
    }
]

#test for update_task()
assert update_task(all_tasks, '1', priority_scale, 'info', 'Call 123-456-7890', 1) == {
        "name": "Call XYZ",
        "info": "Call 123-456-7890",
        "priority": 3,
        "duedate": '05/28/2022',
        "done": 'yes'
    }
assert update_task(all_tasks, '1', priority_scale, 'name', 'Call ABC', 1) == {
        "name": "Call ABC",
        "info": "Call 123-456-7890",
        "priority": 3,
        "duedate": '05/28/2022',
        "done": 'yes'
    }     
#---------------------------------------------------------------------------------
#test for delete_item()
assert delete_item([], 1, 1) == 0
assert delete_item([1], '-2') == -1
assert delete_item([1, 2, 3], '2') == 3
#---------------------------------------------------------------------------------
#test for load_tasks_from_csv()
assert load_tasks_from_csv('missing-date.csv', all_tasks, priority_scale) == [1]
assert load_tasks_from_csv('task', all_tasks, priority_scale) == -1
#test for save_tasks_to_csv()
one_task =[    {
        "name": "Finish checkpoint 1 for CSW8",
        "info": "Submit to Gradescope",
        "priority": 5,
        "duedate": '06/02/2022',
        "done": 'no'
    }]
assert save_tasks_to_csv(one_task, 'hello') == -1
assert save_tasks_to_csv(one_task, 'hello.csv') == None
