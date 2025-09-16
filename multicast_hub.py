import json
import serial

# Configure the serial port
SERIAL_PORT = '/dev/tty.usbserial-A50285BI' 
BAUD_RATE = 9600

def main():
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=3)
    print("Hub started. Enter commands in the format: destination payload_text")
    print("Press Ctrl+C to exit.")

    while True:
        try:
            input_text = input("> ").strip()
            if not input_text:
                continue

            # Split into destination and payload
            parts = input_text.split(maxsplit=1)
            destination = parts[0]
            payload = parts[1] if len(parts) > 1 else ""

            # Create JSON message
            message = {
                "source": "hub",
                "destination": destination,
                "payload": payload
            }
            json_str = json.dumps(message)

            # Send over serial
            print("Sending:", json_str)
            ser.write((json_str + '\r\n').encode())

            # Listen for reply with timeout
            reply_bin = ser.readline()
            reply = reply_bin.decode().strip()
            if reply:
                try:
                    json_reply = json.loads(reply)
                    print("Reply received:", json_reply)
                except json.JSONDecodeError:
                    print("Invalid JSON reply:", reply)
            else:
                print("Timeout: No reply received within 1 second.")
        except KeyboardInterrupt:
            print("\nExiting hub.")
            break
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
