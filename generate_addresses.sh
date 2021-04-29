#!/bin/bash
SECRET=$(cat /var/lib/bee-clef/password)
NUM_ADDRESSES=10
TEMP=$(mktemp /tmp/temporary-file.XXXXXXXX)

counter=1
while [ $counter -le $NUM_ADDRESSES ]
do
        clef --keystore /var/lib/bee-clef/keystore --stdio-ui newaccount --lightkdf > ${TEMP} 2>&1 <<EOF
$SECRET
EOF

        ADDRESS=$(cat ${TEMP} | grep -Po '(?<=Generated account ).*')
        #echo Processing address: $ADDRESS

        clef --keystore /var/lib/bee-clef/keystore --configdir /var/lib/bee-clef --stdio-ui setpw $ADDRESS >/dev/null 2>&1 <<EOF
$SECRET
$SECRET
$SECRET
EOF
        echo "Address $counter: $ADDRESS"
        ((counter++))
done

echo All done
