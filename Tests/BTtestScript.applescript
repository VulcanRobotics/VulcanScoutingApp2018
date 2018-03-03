property device : "zhixuanli"
tell application "Finder" to set fileAlias to selection as alias
set fileToSend to fileAlias
tell application "Finder" to open fileToSend using application file id "com.apple.BluetoothFileExchange"
activate application "Bluetooth File Exchange"
tell application "System Events"
	tell process "Bluetooth File Exchange"
		repeat until exists window 1
		end repeat
		tell application "Bluetooth File Exchange" to browse "zhixuanli"
		#select ((row 1 of table 1 of scroll area 1 of window 1) whose value of UI element 2 of UI element 1 is device)

		#to perform action "AXShowMenu"

		#set btDevice to (row 1 of table 1 of scroll area 1 of window 1) whose value of UI element 2 of UI element 1 is device
		#tell btDevice to perform action "AXShowMenu"
		#click button "Send" of window 1
		#return btDevice
	end tell
end tell
