function handler () {
  EVENT_DATA=$1
  echo "handler event: $EVENT_DATA" 1>&2;

  # Extracting the type value using shell string manipulation
  TYPE=$(echo $EVENT_DATA | sed -e 's/.*"type":"\([^"]*\)".*/\1/')

  if [ "$TYPE" = "good_req" ]; then
    RESPONSE='{"status":"200"}'
  else
    RESPONSE='{"status":"500"}'
  fi

  echo $RESPONSE
}