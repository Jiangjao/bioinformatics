# Exercise 20

## preparation
1. Open the terminal or command line.
2. install lldb.
3. Wait for the installation to complete.
4. Run the lldb command to start the lldb debugger.

## Extra Credit
-   Find a graphical debugger and compare using it to raw gdb. These are useful when the program you're looking at is local, but they are pointless if you have to debug a program on a server.
1. A graphical debugger:
   - A tool that provides a graphical user interface (GUI) for debugging programs.
   - Makes it easier to visualize the program flow, set breakpoints, and inspect variables.

2. Visual Studio Code with C/C++ extension:
   - Provides a user-friendly GUI for easier navigation and interaction.
   - Allows easier setting and management of breakpoints.
   - Offers syntax highlighting, code completion, and function signature support.
   - Has a built-in terminal for executing commands.
   - Supports remote debugging via the Remote - SSH extension.

3. Raw GDB (GNU Debugger):
   - Command-line interface, which might be less intuitive for some users.
   - Requires manual input of commands to navigate through code, set breakpoints, and inspect variables.
   - No syntax highlighting, code completion, or function signature support.
   - Can be used on a local machine or remotely via an SSH connection.

4. Comparison:
   - A graphical debugger like VS Code with C/C++ extension provides a more user-friendly experience compared to raw GDB, making it easier to debug and understand the code.
   - Raw GDB might be more suitable for debugging programs on a server, as it does not require a GUI and can be used remotely via an SSH connection. However, VS Code also supports remote debugging with the Remote - SSH extension.
   - For users already familiar with GDB commands, raw GDB can be more efficient and flexible.

-   You can enable core dumps on your OS, and when a program crashes, you'll get a core file. This core file is like a postmortem of the program that you can load up to see what happened right at the crash and what caused it. Change ex31.c so that it crashes after a few iterations, then try to get a core dump and analyze it.

Sure! Here's an explanation of how to enable core dump mode:

By default, core dump is enabled on most Linux systems. However, some systems may have core dump disabled or limited in size. To enable or modify the core dump settings, you can follow these steps:

1. Check the current core dump settings of the system. You can use the following command to view them:

   ````
   ulimit -a
   ```

   If the `core file size` value in the output is `0`, it means core dump is disabled.

2. If you need to enable core dump, you can use the following command to set the size of the core dump:

   ````
   ulimit -c unlimited
   ```

   This will allow the operating system to generate core dump files of any size when a program crashes.

3. To preserve the core dump settings after a system reboot, you can add the above command to the system startup script (e.g. `/etc/profile` or `/etc/bashrc`).

4. If you need to generate a core dump for a specific program when it crashes, you can add the following command before running the program:

   ````
   ulimit -c unlimited
   ```

   This will generate a core dump file when the program crashes.

It's important to note that core dump files can be very large, so you should ensure that your system has enough disk space before generating a core dump. Additionally, core dump files may contain sensitive information, so you should take measures to protect their security.