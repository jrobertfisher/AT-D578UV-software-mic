# AT-D578UV-software-mic
 AT-D578UV software mic, hex codes, and CAT config info.

 Code: https://github.com/jrobertfisher/AT-D578UV-software-mic

 Wiki: https://github.com/jrobertfisher/AT-D578UV-software-mic/wiki

The AT-D578UV software mic is a software-based solution that emulates the functionality of the physical microphone for the AT-D578UV radio. It utilizes hex codes that correspond to the button presses on the hand microphone to control the radio's operations.

To capture the hex codes, traffic on the wire between the radio and the physical microphone was sniffed. The communication traffic was intercepted to determine the specific hex codes associated with each physical mic button press. These hex codes represent commands that control various features of the radio, such as zone and channel selection, menu browsing, VFO switching, PTT control, and more.

By emulating the hand microphone's functionality through software, the AT-D578UV software mic provides users with an alternative interface to control the radio. This software-based approach offers flexibility and customization options that may not be available with the physical microphone. This also allows the radio to be used without changing the mic control setting from UART to Volt detection.

As for future ideas, one possibility is to explore the integration of the AnyTone BT-01 bluetooth mic. By leveraging the capabilities of the bluetooth mic, it could be possible to create a software-based screen for the radio. This screen could display information such as channel frequencies, signal strength, and other relevant data. Users could interact with this software screen to control the radio and access its features, providing a more intuitive and visually appealing user experience.

Integrating the AnyTone BT-01 bluetooth mic into the software mic solution would require understanding the communication protocol and command structure of the bluetooth mic. Once the protocol is deciphered, the software mic could send appropriate commands and receive responses from the bluetooth mic, enabling wireless interaction with the radio. If you have any information about this idea, please create an issue.

When running the code, be sure to update the port to the correct one for your digirig. The callsign text can also be updated to your callsign.

Software Mic v1.0 Release Notes - Initial Release
Software Mic v1.0.1 Release Notes
    Fixed image paths
    Complied an exe and published it to the dist folder (the exe is hard coded for Com Port 4, I'll add a configuration tab to set the port and call sign info soon.)
Software Mic v1.0.2 Release Notes
    Changed buttons to include IRP_MJ_DEVICE_CONTROL (IOCTL_SERIAL SET and GET), to make clicks more responsive.
    Added a .conf file to manage settings.
    Opens .conf window, then starts connection
    When settings button is pressed, the serial connection is stopped, when the connect button is pressed, the settings are read from the .conf file and a new connection is started.
    Added icons.
    Windows EXE compiled and posted in the dist folder.