
def print_main_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and outputs a question
    "What would you like to do?"
    """
    print("==========================")
    print("What would you like to do?")
    # TODO: Loop-over the dictionary `menu`
    # to print the keys and options
    for item in menu:
        print(f'{item} - {menu[item]}')
    print("==========================")

def get_written_date1(date_string):
    """
    The function takes as a parameter a valid date-string in the 
    <MM>/<DD>/<YEAR> format and returns the resulting date as a string. 
    It would return None if the input is invalid.
    """ 
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    date_list = date_string.split('/')
    month = int(date_list[0])
    date = int(date_list[1])
    year = date_list[2]   
    return f'{month_names[month]} {date}, {year}'

def get_written_date(date_list):
    """
     The function takes as a parameter a valid date-string in the 
    [MM, DD, YYYY] format and returns the resulting date as a string. 
    It would return None if the input is invalid.
    """
    
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    
    month = int(date_list[0])
    date = int(date_list[1])
    year = date_list[2]   
    return f'{month_names[month]} {date}, {year}'

def get_selection(action, suboptions, to_upper = True, go_back = False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu

    The function displays a submenu for the user to choose from. 
    Asks the user to select an option using the input() function. 
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.

    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None
    while selection not in suboptions:
        print(f"::: What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back == True:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper() # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'

    if to_upper:    
        print(f"You selected |{selection}| to",
              f"{action.lower()} |{suboptions[selection].lower()}|.")
    else:
        print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection


def print_task(task, priority_map, name_only = False):
    """
    param: task (dict) - a dictionary object that is expected
            to have the following string keys:
    - "name": a string with the task's name
    - "info": a string with the task's details/description
            (the field is not displayed if the value is empty)
    - "priority": an integer, representing the task's priority
        (defined by a dictionary priority_map)
    - "duedate": a valid date-string in the US date format: <MM>/<DD>/<YEAR>
            (displayed as a written-out date)
    - "done": a string representing whether a task is completed or not

    param: priority_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "priority"
            values stored in the task; the stored value is displayed for the
            priority field, instead of the numeric value.
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the task is printed.
            Otherwise, displays the formatted task fields.

    returns: None; only prints the task values

    Helper functions:
    - get_written_date() to display the 'duedate' field
    """
    if name_only == False:
        print(f'{task["name"]}')
        
        if len(task["info"]) != 0:
            print(f'  * {task["info"]}')
            
        print(f'  * Due: {get_written_date1(task["duedate"])}  (Priority: {priority_map[task["priority"]]})')
        print(f'  * Completed? {task["done"]}')
    else:
        print(f'{task["name"]}')
         
def print_tasks(task_list, priority_map, name_only = False,
                show_idx = False, start_idx = 0, completed = "all"):
    """
    param: task_list (list) - a list containing dictionaries with
            the task data
    param: priority_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "priority"
            values stored in the task; the stored value is displayed 
            for the priority field, instead of the numeric value.
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the task is printed.
            Otherwise, displays the formatted task fields.
            Passed as an argument into the helper function.
    param: show_idx (Boolean) - by default, set to False.
            If False, then the index of the task is not displayed.
            Otherwise, displays the "{idx + start_idx}." before the
            task name.
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets displayed for the first task, if show_idx is True.
    param: completed (str) - by default, set to "all".
            By default, prints all tasks, regardless of their
            completion status ("done" field status).
            Otherwise, it is set to one of the possible task's "done"
            field's values in order to display only the tasks with
            that completion status.

    returns: None; only prints the task values from the task_list

    Helper functions:
    - print_task() to print individual tasks
    """
    print("-"*42)
    for task in task_list: # go through all tasks in the list
        if show_idx: # if the index of the task needs to be displayed
            idx = task_list.index(task)
            print(f"{idx + start_idx}.", end=" ")
        if completed == "all":
            print_task(task, priority_map, name_only)
        elif task["done"] == completed:
            print_task(task, priority_map, name_only)
#---------------------------------------------------------------------------------
def get_new_task(a_five_string_list, priority_scale):
    """
    Document the function correctly
    """
    if len(a_five_string_list) != 5:
        return len(a_five_string_list)
    for i in a_five_string_list:
        if type(i) != str:
            return tuple(["type", i])
    if is_valid_name(a_five_string_list[0]) == False:
        return tuple(["name", a_five_string_list[0]]) 
    if is_valid_priority(a_five_string_list[2], priority_scale) == False:    
        return tuple(["priority", a_five_string_list[2]])          
    if is_valid_date(a_five_string_list[3]) == False:
        return tuple(["duedate", a_five_string_list[3]])
    if is_valid_completion(a_five_string_list[4]) == False:         
        return tuple(["done", a_five_string_list[4]])       
    return {
             "name": a_five_string_list[0],
             "info": a_five_string_list[1],
             "priority": int(a_five_string_list[2]),
             "duedate": a_five_string_list[3],
             "done": a_five_string_list[4]
            }                

def is_valid_name(name_string):
    '''The function take value of "name" key in and check the validation '''
    if 3<=len(name_string) and len(name_string)<=25:
        return True
    else:
        return False

def is_valid_priority(priority_string, priority_scale):
    '''The function take value of "priority" key in and check the validation '''
    if str(priority_string).isdigit() == True:
        if int(priority_string) in priority_scale:
            return True
    return False    

def is_valid_month(date_string):
    """
    The function takes in a list of strings in the (MM/DD/YYYY) 
    format to determine whether the month is between 1 and 12.
    """
    # TODO: Finish the function
    date_list = date_string.split('/')
    if type(date_list[0])== str:
        month = date_list[0]
        if month.isdigit():
            if 1<=int(month) and int(month)<=12:
                return True
    return False
def is_valid_day(date_string):
    """
    The function takes in a list of strings in the (MM/DD/YYYY) 
    format to determine whether the day in each month is in range.
    """
    date_list = date_string.split('/')
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    # TODO: Finish the function
    month = date_list[0]
    day = date_list[1]
    if type(date_list[1])== str:
        if day.isdigit():
            if is_valid_month(date_string) == True:
                if num_days[int(month)]>= int(day):
                    return True
    return False
def is_valid_year(date_string):
    """
    The function takes in a list of strings in the (MM/DD/YYYY) 
    format to determine whether the year is a positive integer and greater than 1000.
    """
    date_list = date_string.split('/')
    year = date_list[2]
    if type(date_list[2])== str:
        if int(year)>1000:
            return True
    return False
def is_valid_date(date_string):
    '''The function take value of "duedate" key in and check the validation '''
    if is_valid_month(date_string) == False:
        return False       
    if is_valid_day(date_string) == False:
        return False
    if is_valid_year(date_string) == False:
        return False
    return True
    
def is_valid_completion(comple_string):
    '''The function take value of "done" key in and check the validation '''
    if comple_string == "yes" or comple_string == "no":
        return True
    else:
        return False
#---------------------------------------------------------------------------------
def is_valid_index(idx, in_list, start_idx = 0):
    """
    param: idx (str) - a string that is expected to
            contain an integer index to validate
    param: in_list - a list that the idx indexes
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing

    The function checks if the input string contains
    only digits and verifies that (idx - start_idx) is >= 0,
    which allows to retrieve an element from in_list.

    returns:
    - True, if idx is a numeric index >= start_idx
    that can retrieve an element from in_list.
    - False if idx is not a string that represents an 
    integer value, if int(idx) is < start_idx,
    or if it exceeds the size of in_list.
    """
    if type(idx)!= str:
        return False
    if idx.isdigit() == False:
        return False
    if int(idx) < start_idx:
        return False
    if int(idx)-start_idx > (len(in_list)-1):
        return False
    return True

def update_task(info_list, idx, priority_map, field_key, field_info, start_idx = 0):
    """
    param: info_list - a list that contains task dictionaries
    param: idx (str) - a string that is expected to contain an integer
            index of an item in the input list
    param: start_idx (int) - by default is set to 0;
            an expected starting value for idx that gets subtracted
            from idx for 0-based indexing
    param: priority_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the priority value "Highest" or "Low")
            Needed if "field_key" is "priority" to validate its value.
    param: field_key (string) - a text expected to contain the name
            of a key in the info_list[idx] dictionary whose value needs to 
            be updated with the value from field_info
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            info_list[idx][field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key.

    The function first calls one of its helper functions
    to validate the idx and the provided field.
    If validation succeeds, the function proceeds with the update.

    return:
    If info_list is empty, return 0.
    If the idx is invalid, return -1.
    If the field_key is invalid, return -2.
    If validation passes, return the dictionary info_list[idx].
    Otherwise, return the field_key.

    Helper functions:
    The function calls the following helper functions:
    - is_valid_index()
    Depending on the field_key, it also calls:
    - is_valid_name()
    - is_valid_priority()
    - is_valid_date()
    - is_valid_completion()
    """
    if len(info_list) == 0:
        return 0
    if is_valid_index(idx, info_list) == False:
        return -1
    if field_key not in info_list[int(idx)-start_idx]:
        return -2
    if field_key == 'name':
        if is_valid_name(field_info) == True:
            info_list[int(idx)-start_idx]['name']=field_info
            return info_list[int(idx)-start_idx]
    if field_key == 'info':
        info_list[int(idx)-start_idx]['info']=field_info
        return info_list[int(idx)-start_idx]         
    if field_key == 'priority':        
        if is_valid_priority(field_info, priority_map) == True:
            info_list[int(idx)-start_idx]['priority']= int(field_info)
            return info_list[int(idx)-start_idx]
    if field_key == 'duedate':
        if is_valid_date(field_info) == True:
            info_list[int(idx)-start_idx]['duedate']=field_info
            return info_list[int(idx)-start_idx]
    if field_key == 'done':        
        if is_valid_completion(field_info) == True:
            info_list[int(idx)-start_idx]['done']=field_info
            return info_list[int(idx)-start_idx]
    return field_key
#---------------------------------------------------------------------------------
def delete_item(in_list, idx, start_idx = 0):
    """
    param: in_list - a list from which to remove an item
    param: idx (str) - a string that is expected to
            contain a representation of an integer index
            of an item in the provided list
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing

    The function first checks if the input list is empty.
    The function then calls is_valid_index() to verify
    that the provided index idx is a valid positive
    index that can access an element from info_list.
    On success, the function saves the item from info_list
    and returns it after it is deleted from in_list.

    returns:
    If the input list is empty, return 0.
    If idx is not of type string or start_idx is not an int, return None.
    If is_valid_index() returns False, return -1.
    Otherwise, on success, the function returns the element
    that was just removed from the input list.

    Helper functions:
    - is_valid_index()
    """
    if len(in_list) == 0:
        return 0
    if type(idx) != str or type(start_idx) != int:
        return None
    if is_valid_index(idx, in_list, start_idx) == False:
        return -1
    remove_item = in_list[int(idx)-start_idx]
    in_list.pop(int(idx)-start_idx)
    return remove_item
#---------------------------------------------------------------------------------
def load_tasks_from_csv(filename, in_list, priority_map):
    """
    param: filename (str) - A string variable that represents the
            name of the file from which to read the contents.
    param: in_list (list) - A list of task dictionary objects to which
            the tasks read from the provided filename is appended.
            If in_list is not empty, the existing tasks are not dropped.
    param: priority_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the priority value "Highest" or "Low")
            Needed by the helper function.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` and `import os`.

    If the file exists, the function will use the `with` statement to open the
    `filename` in "read" mode. For each row in the csv file, the function will
    proceed to create a new task using the `get_new_task()` function.
    - If the function `get_new_task()` returns a valid task object,
    it gets appended to the end of the `in_list`.
    - If the `get_new_task()` function returns an error, the 1-based
    row index gets recorded and added to the NEW list that is returned.
    E.g., if the file has a single row, and that row has invalid task data,
    the function would return [1] to indicate that the first row caused an
    error; in this case, the `in_list` would not be modified.
    If there is more than one invalid row, they get excluded from the
    in_list and their indices will be appended to the new list that's
    returned.

    returns:
    * -1, if the last 4 characters in `filename` are not '.csv'
    * None, if `filename` does not exist.
    * A new empty list, if the entire file is successfully read from `in_list`.
    * A list that records the 1-based index of invalid rows detected when
      calling get_new_task().

    Helper functions:
    - get_new_task()
    """
    import csv
    import os
    if filename[-4:] != '.csv':
        return -1
    if os.path.exists(filename) == False:
        return None   
    empty_list = []
    fail_list = []
    with open(filename, 'r') as csvfile:
        new_list_reader = csv.reader(csvfile, delimiter=',')
        count=0
        for row in new_list_reader:
            count+=1
            for item in row:
                empty_list.append(item)
            if type(get_new_task(empty_list, priority_map)) == dict:
                in_list.append(get_new_task(empty_list, priority_map))
                
            else: 
                fail_list.append(count)
        if len(fail_list)!=0:
            return fail_list
#---------------------------------------------------------------------------------
def save_tasks_to_csv(tasks_list, filename):
    """
    param: tasks_list - The list of the tasks stored as dictionaries
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the tasks. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every task in the list and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the list is:

    * `name` field of the task dictionary
    * `info` field of the task dictionary
    * `priority` field of the task as a string
    (i.e, "5" or "3", NOT "Lowest" or "Medium")
    * `duedate` field of the task as written as string
    (i.e, "06/06/2022", NOT "June 6, 2022")
    * `done` field of the task dictionary

    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    import csv
    if filename[-4:] != '.csv':
        return -1
    
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for task in tasks_list:
            new_list = []
            new_list.append(task['name'])  
            new_list.append(task['info'])
            new_list.append(str(task['priority']))
            new_list.append(task['duedate'])
            new_list.append(task['done'])           
            csv_writer.writerow(new_list)

    

            