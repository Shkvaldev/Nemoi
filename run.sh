if_util_exists() {
	if ! [ -x "$(command -v $1)" ]; then
	  echo 1;
	  return;
	fi
	echo 0;
}

if_file_exists() {
	if ! [ -f "$1" ]; then
	    echo 1;
	    return;
	fi
	echo 0;
}