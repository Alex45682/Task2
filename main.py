from os import walk
from zipfile import ZipFile
import os.path
import datetime
import logging

lvl = {1: "INFO", 2: "DEBUG"}

extensions = {
    1: '.txt',
    2: '.csv',
    3: '.dsv'
}


def log_file_path_input():
    log_file_path = (input("Please provide a path for new log file (with extension '.log')"))
    print("Your path to to log file is: {}".format(log_file_path))

    return log_file_path


def log_level_input():
    log_level = 0

    while log_level not in ['1', '2']:
        log_level = (input('Which log level you want to use: 1 - INFO, 2 - DEBUG'))

    print("Your log level is: {}".format(lvl[int(log_level)]))

    return int(log_level)


def file_extension_input():
    file_extension = int(input(
        'Files with what extension do you want to archive? 1 - "txt", 2 - "csv", 3 - "dsv": '))
    message = 'Files with extension: {} were selected for archiving'.format(extensions[file_extension])

    print(message)
    logging.info(message)
    return file_extension


def source_folder_input():
    source_folder = (input('Please provide a path for source folder'))

    logging.info('Source folder with path: {} is selected'.format(source_folder))
    print("Your path for source folder is: {}".format(source_folder))
    return source_folder


def output_file_path_input():
    output_path = (input('Please provide a path for output file '))

    print("Your path for output folder is: {}".format(output_path))
    logging.info('Output folder with path: {} is selected'.format(output_path))
    return output_path


def input_menu():
    log_level = log_level_input()
    print("* * * *")
    log_file_path = log_file_path_input()  # example --> /Users/store/PycharmProjects/SecondTask/logs/new_log.log
    print("* * * *")

    open(log_file_path, "w+")

    level = logging.INFO if log_level == 1 else logging.DEBUG
    logging.basicConfig(filename=log_file_path, level=level)

    logging.info('Started')
    logging.info('Log file with path {} is created'.format(log_file_path))
    logging.info('Log level: {} is selected'.format(lvl[int(log_level)]))

    file_extension = file_extension_input()
    print("* * * *")

    source_folder = source_folder_input()  # example --> /Users/store/PycharmProjects/SecondTask/files
    print("* * * *")

    output_path = output_file_path_input()  # example --> /Users/store/PycharmProjects/SecondTask
    print("* * * *")

    return {"source_folder": source_folder, "output_path": output_path, "extension": extensions[file_extension]}


def generate_zip_file_name():
    date = datetime.date.today()
    name = str(date)
    return name + ".zip"


def zip_files(source_folder, output_path, extension):
    f = []
    files_with_needed_extension = []
    for (dirpath, dirnames, filenames) in walk(source_folder):
        f.extend(filenames)

    for file in f:
        if extension in file:
            files_with_needed_extension.append(file)

    file_name = generate_zip_file_name()
    zipObj = ZipFile(file_name.format(output_path + "/" + file_name), 'w')

    for i in files_with_needed_extension:
        zipObj.write(os.path.abspath(source_folder + "/" + i))

    logging.info("Zip file with name {} is created".format(file_name))

    logging.info("Finished")


params = input_menu()
zip_files(params['source_folder'], params['output_path'], params['extension'])
