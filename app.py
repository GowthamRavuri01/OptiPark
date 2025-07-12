import streamlit as st
import datetime

# Set rate per hour for parking
RATE_PER_HOUR = 50
GST_RATE = 0.18  # 18% GST
SERVICE_CHARGE = 10  # Fixed service charge in INR


def main():
    # Create a centered column layout
    col_center = st.columns([1, 3, 1])  # Center alignment using column layout

    with col_center[1]:  # Center content in the middle column
        # Create two columns inside the centered column for the image and title
        col1, col2 = st.columns([1, 8])  # Adjust widths for alignment
        
        with col1:
            st.image("optipark_icon1.png", width=60)  # Adjust width if needed

        with col2:
            # Display the website title with enhanced styling
            st.markdown("""
            <div style="text-align: left;">
                <h1 style="font-size: 50px; color: white; font-weight: bold; display: inline;">OPTIPARK</h1>
                <p style="font-size: 15px; color: white; font-style: italic; font-family: 'Arial, sans-serif';">Parking made effortless.</p>
            </div>
            """, unsafe_allow_html=True)


    # User Input Section
    st.header("Enter Parking Details")

    username = st.text_input("User Name")
    mobile = st.text_input("Mobile Number")
    location = st.text_input("Current Location")
    vehicle = st.text_input("Vehicle Number")

    # Parking Duration
    duration = st.number_input("Parking Duration (in hours)", min_value=1, max_value=24, value=1)
    start_time = st.time_input("Start Time (HH:MM)")

    # Generate time slot options
    start_time_obj = datetime.datetime.combine(datetime.date.today(), start_time)
    end_time_obj = start_time_obj + datetime.timedelta(hours=duration)
    time_slot = f"{start_time_obj.strftime('%H:%M')} to {end_time_obj.strftime('%H:%M')}"
    st.write(f"Selected Time Slot: {time_slot}")

    # Display Available Parking Lots and Billing Information
    if st.button("Submit"):
        if username and mobile and location and vehicle:
            # Calculate base price and total price with taxes
            base_price = duration * RATE_PER_HOUR
            gst_amount = base_price * GST_RATE
            total_price = base_price + gst_amount + SERVICE_CHARGE

            # Display Results
            st.header("Available Parking Lots")
            st.write("Below are the available parking lots based on your selected time slot.")

            # Display Parking Summary
            st.header("Parking Summary")
            st.write(f"**User Name:** {username}")
            st.write(f"**Mobile Number:** {mobile}")
            st.write(f"**Location:** {location}")
            st.write(f"**Vehicle Number:** {vehicle}")
            st.write(f"**Parking Duration:** {duration} hours")
            st.write(f"**Time Slot:** {time_slot}")
            st.write(f"**Base Price:** Rs.{base_price}")

            # Display Total Bill as a Separate Section
            st.header("Total Bill")
            st.write(f"**GST (18%):** Rs.{gst_amount:.2f}")
            st.write(f"**Service Charge:** Rs.{SERVICE_CHARGE}")
            st.write(f"**Total Price:** Rs.{total_price:.2f}")

        else:
            st.warning("Please fill in all the fields")

if __name__ == "__main__":
    main()
