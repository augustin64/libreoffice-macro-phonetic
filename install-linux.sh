#!/bin/sh
mkdir "$HOME/.config/libreoffice/4/user/Scripts/python" --parent

pip install bs4 requests

cp "./phonetic-macro.py" "$HOME/.config/libreoffice/4/user/Scripts/python/"


echo -e "\n\n\n\n\t====================\n"
echo "Script added to folder, start libreoffice writer"
echo -e "and bind a keyboard shortcut to it in\n"

echo "Tools > Customize > Keyboard"
echo "Select a key, then go to "
echo "Category > LibreOffice Macros > My Macros > wordreference > Function insert_phonetic"
echo -e "and press the \"modify\" button to apply changes\n\n"


echo "You can then select text and press your keyboard shortcut to inser phonetic."
echo "If at this point, it's not working on your computer,"
echo "please make sure you have valid JRE and python intallation,"
echo -e "then re-run this script.\n"

echo -e "And if you still encounter an issue, please file the bug at https://github.com/augustin64/libreoffice-macro-phonetic\n\n\t====================\n"
