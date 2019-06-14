from myapp.models import *

def create_test():
    test = Test()
    test.name = 'Linux test 1'
    test.save()

    q = saveQuestion(test, 'One of the jobs of the kernel is to:')
    saveChoice(q, 'Transfer mail from one machine to another')
    saveChoice(q, 'Manage the system’s resources', True)
    saveChoice(q, 'Load the operating system after the computer is turned on')
    saveChoice(q, 'Turn source code into machine code')
    
    q = saveQuestion(test, 'Linux is written in:')
    saveChoice(q, 'C', True)
    saveChoice(q, '.NET')
    saveChoice(q, 'Java')
    saveChoice(q, 'Perl')
    saveChoice(q, 'C++')

    q = saveQuestion(test, 'Source code refers to:')
    saveChoice(q, 'The interface that software uses to talk to the kernel')
    saveChoice(q, 'The license that dictates how you may use and share the software')
    saveChoice(q, 'The version of a program that the computer runs on the CPU')
    saveChoice(q, 'A human readable version of computer software', True)

    q = saveQuestion(test, 'Most of the tools that are part of Linux systems come from:')
    saveChoice(q, 'Google')
    saveChoice(q, 'Red Hat and Debian')
    saveChoice(q, 'The Open Source Initiative')
    saveChoice(q, 'The Linux foundation')
    saveChoice(q, 'The GNU project', True)

    q = saveQuestion(test, 'The Linux platform that runs on mobile phones is called:')
    saveChoice(q, 'IOS')
    saveChoice(q, 'Teldroid')
    saveChoice(q, 'LinuxMobile')
    saveChoice(q, 'Android', True)
    saveChoice(q, 'MicroLinux')

    q = saveQuestion(test, 'What does a distribution provide to add and remove software from the system?')
    saveChoice(q, 'Bash')
    saveChoice(q, 'Application Programming Interface (API)')
    saveChoice(q, 'Partitioning tool')
    saveChoice(q, 'Package manager', True)
    saveChoice(q, 'Compiler')

    q = saveQuestion(test, 'The bootloader’s job is to:')
    saveChoice(q, 'The bootloader’s job is to:')
    saveChoice(q, 'Assign initial settings such as network address')
    saveChoice(q, 'Install software from the Internet or removable media')
    saveChoice(q, 'Perform the initial installation of the kernel to hard drive')
    saveChoice(q, 'Load the kernel after the computer is powered on', True)

    q = saveQuestion(test, 'UNIX was originally invented at:')
    saveChoice(q, 'Stanford University')
    saveChoice(q, 'AT&T Bell Labs', True)
    saveChoice(q, 'Berkeley University')
    saveChoice(q, 'Xerox PARC')
    saveChoice(q, 'Bangalore University')

    q = saveQuestion(test, 'A license where you don’t have access to the source code is called:')
    saveChoice(q, 'Impaired source')
    saveChoice(q, 'Closed source', True)
    saveChoice(q, 'Open source')
    saveChoice(q, 'Sourceless')

    q = saveQuestion(test, 'Ubuntu is derived from which distribution?')
    saveChoice(q, 'Scientific Linux')
    saveChoice(q, 'Slackware')
    saveChoice(q, 'Fedora')
    saveChoice(q, 'Debian', True)
    saveChoice(q, 'Red Hat Enterprise Linux')

    q = saveQuestion(test, 'Applications make requests to the kernel and receive resources, such as memory, CPU, and disk in return. True or False?')
    saveChoice(q, 'True', True)
    saveChoice(q, 'False')

    q = saveQuestion(test, 'The most important consideration when choosing an operating system is:')
    saveChoice(q, 'What the computer will do', True)
    saveChoice(q, 'The licensing model of the operating system')
    saveChoice(q, 'The operating system’s mascot')
    saveChoice(q, 'How much performance is needed')
    saveChoice(q, 'Whether or not it is cloud-friendly')

    q = saveQuestion(test, 'Linux is not Unix because:')
    saveChoice(q, 'It’s not good enough')
    saveChoice(q, 'It’s free')
    saveChoice(q, 'It’s not made by the Open Group')
    saveChoice(q, 'There are too many distributions')
    saveChoice(q, 'It hasn’t undergone certification', True)

    q = saveQuestion(test, 'A release cycle:')
    saveChoice(q, 'Is always 6 months')
    saveChoice(q, 'Doesn’t matter in an Open Source environment')
    saveChoice(q, 'Describes how long the software will be supported for')
    saveChoice(q, 'Describes how often updates to the software come out', True)
    saveChoice(q, 'Only applies to software you pay for')

    q = saveQuestion(test, 'A maintenance cycle:')
    saveChoice(q, 'Should be long so that you have time before you need to upgrade')
    saveChoice(q, 'Only has meaning for paid software')
    saveChoice(q, 'Should be short so you always have the freshest releases')
    saveChoice(q, 'Describes how often updates for software come out')
    saveChoice(q, 'Describes how long a version of software will be supported', True)

    q = saveQuestion(test, 'Software is backward compatible if:')
    saveChoice(q, 'It still supports old file formats or applications', True)
    saveChoice(q, 'It can be upgraded without downtime')
    saveChoice(q, 'If the next version still works the same way')
    saveChoice(q, 'It works across Linux/Mac/Windows')
    saveChoice(q, 'People still use old versions')

    q = saveQuestion(test, 'The _____ command displays information about the Linux kernel:')
    saveChoice(q, 'kern')
    saveChoice(q, 'uname', True)
    saveChoice(q, 'real')
    saveChoice(q, 'linux')

    q = saveQuestion(test, 'The [ ] characters around day in the example cal [-smjy13] [[[day] month] year] means that day is:')
    saveChoice(q, 'An option, not an argument')
    saveChoice(q, 'Required')
    saveChoice(q, 'An argument that must be “day” and nothing else')
    saveChoice(q, 'Optional', True)

    q = saveQuestion(test, 'The syntax [-u|–utc|–universal] means:')
    saveChoice(q, 'These are required options')
    saveChoice(q, 'These three options are different')
    saveChoice(q, 'These three options mean the same thing', True)
    saveChoice(q, 'This is invalid syntax')

    q = saveQuestion(test, 'If you want to delete a variable, you can run:')
    saveChoice(q, 'delete')
    saveChoice(q, 'unset', True)
    saveChoice(q, 'clear')
    saveChoice(q, 'wipe')

    q = saveQuestion(test, 'Local variables are:')
    saveChoice(q, 'Only available to the shell they are created in', True)
    saveChoice(q, 'Passed into other shells and commands')
    saveChoice(q, 'Are not a valid type of variable')
    saveChoice(q, 'Not used by shells at all')

    q = saveQuestion(test, 'Which of the following is a valid way to add the /data directory to the existing PATH variable?')
    saveChoice(q, 'PATH=$PATH:/data', True)
    saveChoice(q, 'PATH=/data')
    saveChoice(q, '$PATH=/data')
    saveChoice(q, '$PATH=$PATH:/data')

    q = saveQuestion(test, 'To view all processes on the system, you can execute:')
    saveChoice(q, 'ps -f')
    saveChoice(q, 'ps –all')
    saveChoice(q, 'ps -e', True)
    saveChoice(q, 'ps')

    q = saveQuestion(test, 'In order to run a command called “tough” in the background, you would type:')
    saveChoice(q, 'tough@')
    saveChoice(q, 'bg tough')
    saveChoice(q, 'tough&', True)
    saveChoice(q, 'start -b tough')

    q = saveQuestion(test, 'To send a signal to a set of processes with the same name, you can run:')
    saveChoice(q, 'killall', True)
    saveChoice(q, 'grpkill')
    saveChoice(q, 'allkill')
    saveChoice(q, 'sigkill')

    q = saveQuestion(test, 'Which of the following is not used for globbing?')
    saveChoice(q, '#', True)
    saveChoice(q, '*')
    saveChoice(q, '?')
    saveChoice(q, '[')



def saveQuestion(test, text):
    q = Question()
    q.test = test
    q.text = text
    q.save()
    return q

def saveChoice(question, text, is_right_ancwer=False):
    ch = Choice()
    ch.question = question
    ch.text = text
    ch.is_right_answer = is_right_ancwer
    ch.save()

