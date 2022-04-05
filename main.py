from os import walk
from zipfile import ZipFile
import os.path
import datetime
import logging


def menu():
    lvl = {1: "INFO", 2: "DEBUG"}

    log_level = (input('Which log level you want to use: 1 - INFO, 2 - DEBUG'))
    print("Your log level is: {}".format(lvl[int(log_level)]))
    print("* * * *")

    log_file_path = (input("Please provide a path for new log file (with extension '.log')"))
    print("Your path to to log file is: {}".format(log_file_path))
    # example --> /Users/store/PycharmProjects/SecondTask/logs/new_log.log
    print("* * * *")

    open(log_file_path, "w+")

    logging.basicConfig(filename=log_file_path, level=logging.INFO if log_level == 1 else logging.DEBUG)

    logging.info('Started')

    logging.info('Log file with path {} is created'.format(log_file_path))

    logging.info('Log level: {} is selected'.format(lvl[int(log_level)]))

    extensions = {
        1: '.txt',
        2: '.csv',
        3: '.dsv'
    }

    file_extension = int(input(
        'Files with what extension do you want to archive? 1 - "txt", 2 - "csv", 3 - "dsv": '))
    message = 'Files with extension: {} were selected for archiving'.format(extensions[file_extension])

    print(message)
    logging.info(message)
    print("* * * *")

    source_folder = (input('Please provide a path for source folder'))
    # example --> /Users/store/PycharmProjects/SecondTask/files

    logging.info('Source folder with path: {} is selected'.format(source_folder))
    print("Your path for source folder is: {}".format(source_folder))
    print("* * * *")

    output_path = (input('Please provide a path for output file '))
    # example --> /Users/store/PycharmProjects/SecondTask

    print("Your path for output folder is: {}".format(output_path))
    logging.info('Output folder with path: {} is selected'.format(output_path))
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
        break
    for file in f:
        if extension in file:
            files_with_needed_extension.append(file)

    file_name = generate_zip_file_name()
    zipObj = ZipFile(file_name.format(output_path + "/" + file_name), 'w')

    for i in files_with_needed_extension:
         zipObj.write(os.path.abspath(source_folder + "/" + i))

    logging.info("Zip file with name {} is created".format(file_name))
    zipObj.close()

    logging.info("Finished")

props = menu()
zip_files(props['source_folder'], props['output_path'], props['extension'])




