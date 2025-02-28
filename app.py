import streamlit as st
import pandas as pd  # Make sure to import pandas at the top of your file

# Set the title of the app with a custom class
st.markdown("<h1 class='main-header'>Honda Civic Story</h1>", unsafe_allow_html=True)

# New feature: Theme toggle
theme = st.sidebar.radio("Select Theme", ["Light Mode", "Dark Mode"])

# Apply CSS based on the selected theme
if theme == "Dark Mode":
    st.markdown(
        """
        <style>
        body {
            background-image: url('https://example.com/path/to/your/background.jpg'); /* Replace with your image URL */
            background-size: cover; /* Cover the entire background */
            color: white;
        }
        .main-header {
            color: #00f900;  /* Change header color for dark mode */
        }
        .sidebar .sidebar-content {
            background-color: #333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        body {
            background-image: url('https://th.bing.com/th/id/OIP.wDdA3DAPhMtTD3SBk6G0TwHaFj?rs=1&pid=ImgDetMain'); /* Replace with your image URL */
            background-size: cover; /* Cover the entire background */
            background-position: center; /* Center the background image */
            color: black;
        }
        .main-header {
            color: #000;  /* Change header color for light mode */
        }
        .sidebar .sidebar-content {
            background-color: #f0f0f0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Create a sidebar for navigation
options = st.sidebar.radio("", ["Home", "About Us", "Services", "Pictures", "Contact"])

# Define the content for each page
if options == "Home":
    st.header("Welcome to Our Car Website!")
    st.write("Here you can find the best cars available.")

    # New feature: Professional information
    st.subheader("Why Choose Us?")
    st.write("At Honda Civic Story, we pride ourselves on our extensive knowledge and experience in the automotive industry. "
             "Our team is dedicated to providing top-notch services and ensuring customer satisfaction. "
             "With over 20 years of experience, we understand the needs of our customers and strive to meet them with excellence.")
    
    st.subheader("Our Expertise")
    st.write("We specialize in:\n"
             "- **Car Sales**: Offering a wide selection of new and used vehicles.\n"
             "- **Car Rentals**: Flexible rental options to suit your needs.\n"
             "- **Maintenance and Repairs**: Comprehensive services to keep your vehicle in optimal condition.")
    
    # New feature: Car type selection
    st.subheader("Select Your Favorite Car Type")
    car_types = st.selectbox("Choose a car type:", ["Sedan", "SUV", "Hatchback", "Coupe", "Convertible"])
    st.write(f"You selected: **{car_types}**")

    # New feature: Slider for featured cars
    st.subheader("Featured Cars")
    featured_cars = st.slider("Select the number of featured cars to display:", 1, 5, 3)  # Min, Max, Default
    st.write(f"Displaying **{featured_cars}** featured cars.")

    # New feature: Button to show a message
    if st.button("Show More Information"):
        st.write("Thank you for your interest! We have a wide range of cars available for you to explore.")

    # New feature: Customer Testimonials
    st.subheader("Customer Testimonials")
    testimonials = [
        "I had a fantastic experience buying my car! Highly recommend Honda Civic Story!",
        "The service was excellent, and the staff was very helpful.",
        "I love my new car! Thank you for making the process so easy."
    ]
    for testimonial in testimonials:
        st.write(f"- {testimonial}")

    # New feature: Chart showing popular car models
    st.subheader("Popular Car Models")
    car_models = ["Civic", "Accord", "CR-V", "Fit", "HR-V"]
    sales_data = [150, 120, 100, 80, 60]  # Example sales data

    # Create a DataFrame
    data = pd.DataFrame({
        'Car Model': car_models,
        'Sales': sales_data
    })

    # Use the DataFrame to create the bar chart
    st.bar_chart(data.set_index('Car Model'))  # Set 'Car Model' as the index

    # New feature: Interactive map to show dealership location
    st.subheader("Our Location")
    st.map()  # This will show a default map centered on the user's location

    # New feature: Car Pictures Section
    st.subheader("Pictures")
    st.write("Here are some amazing car pictures!")

    # List of car image URLs
    car_images = [
        'https://th.bing.com/th/id/R.4f89213f774b115472eb69107880db25?rik=9WQTmcU%2b1bn3pQ&riu=http%3a%2f%2ftopcarspecs.com%2fmanufacturers%2fhonda%2fhonda-civic%2fhonda-civic-hatchback-modified%2fhonda-civic-hatchback-modified-5.jpg&ehk=LZ3%2fQgAgrZ4aAHeczq4wIay8Cekg7L318IEuqnljyOk%3d&risl=&pid=ImgRaw&r=0',
        'https://th.bing.com/th/id/OIP.HuNW2y8EW8RESzrQfAD0IwHaE8?rs=1&pid=ImgDetMain',
        'https://th.bing.com/th/id/OIP.j5Wu6m8Ti9pD4brlnLnHFgHaFj?w=1000&h=750&rs=1&pid=ImgDetMain',
        'https://th.bing.com/th/id/OIF.tmLmF8au1XAzWZ6od1x4YQ?rs=1&pid=ImgDetMain',
        'https://swaautosports.com/cdn/shop/products/gtr_2_1445x.jpg?v=1668838152',
        'https://th.bing.com/th/id/OIP.v38vysBO64suDfjqYVOIaQHaEK?rs=1&pid=ImgDetMain',
        'https://th.bing.com/th/id/OIP.gu8yOFSJaDCTGb5CphuAqQHaE8?w=1024&h=683&rs=1&pid=ImgDetMain',  # New image link 1
        'https://hips.hearstapps.com/hmg-prod/images/img-7295-10-1666813703.jpg?resize=2048:*',  # New image link 2
        'https://th.bing.com/th/id/OIP.BpSY2oFuzFObCPsk3r4jWAAAAA?rs=1&pid=ImgDetMain'   # New image link 3
    ]

    # Create a grid layout for the images
    cols = st.columns(2)  # Create 2 columns for the grid
    for i, img_url in enumerate(car_images):
        with cols[i % 2]:  # Use modulo to place images in the correct column
            st.image(img_url, use_container_width=True)

            # New feature: Color Picker with unique key
            predefined_colors = ["#00f900", "#ff5733", "#33c1ff", "#ff33a1", "#f0f0f0", "#1e1e1e"]
            selected_color = st.selectbox("Select a predefined color:", predefined_colors, index=0, key=f"predefined_color_{i + 1}")
            custom_color = st.color_picker("Or pick a custom color:", "#00f900", key=f"color_picker_{i + 1}")  # Unique key
            
            # Use the selected predefined color if chosen, otherwise use the custom color
            final_color = selected_color if selected_color else custom_color
            st.write(f"You picked: {final_color}")

            # New feature: Download button
            st.download_button(
                label="Download Image",
                data=img_url,
                file_name=f"car_image_{i + 1}.jpg",
                mime="image/jpeg"
            )

elif options == "Pictures":
    st.header("Pictures")
    st.write("Here are some amazing Honda Civic pictures!")

    # List of car image URLs
    car_images = [
        'https://th.bing.com/th/id/R.4f89213f774b115472eb69107880db25?rik=9WQTmcU%2b1bn3pQ&riu=http%3a%2f%2ftopcarspecs.com%2fmanufacturers%2fhonda%2fhonda-civic%2fhonda-civic-hatchback-modified%2fhonda-civic-hatchback-modified-5.jpg&ehk=LZ3%2fQgAgrZ4aAHeczq4wIay8Cekg7L318IEuqnljyOk%3d&risl=&pid=ImgRaw&r=0',
        'https://th.bing.com/th/id/OIP.HuNW2y8EW8RESzrQfAD0IwHaE8?rs=1&pid=ImgDetMain',
        'https://th.bing.com/th/id/OIP.j5Wu6m8Ti9pD4brlnLnHFgHaFj?w=1000&h=750&rs=1&pid=ImgDetMain',
        'https://th.bing.com/th/id/OIF.tmLmF8au1XAzWZ6od1x4YQ?rs=1&pid=ImgDetMain',
        'https://swaautosports.com/cdn/shop/products/gtr_2_1445x.jpg?v=1668838152',
        'https://th.bing.com/th/id/OIP.v38vysBO64suDfjqYVOIaQHaEK?rs=1&pid=ImgDetMain',
        'https://th.bing.com/th/id/OIP.gu8yOFSJaDCTGb5CphuAqQHaE8?w=1024&h=683&rs=1&pid=ImgDetMain',  # New image link 1
        'https://hips.hearstapps.com/hmg-prod/images/img-7295-10-1666813703.jpg?resize=2048:*',  # New image link 2
        'https://th.bing.com/th/id/OIP.BpSY2oFuzFObCPsk3r4jWAAAAA?rs=1&pid=ImgDetMain'   # New image link 3
    ]

    # Create a grid layout for the images
    cols = st.columns(2)  # Create 2 columns for the grid
    for i, img_url in enumerate(car_images):
        with cols[i % 2]:  # Use modulo to place images in the correct column
            st.image(img_url, use_container_width=True)

            # New feature: Color Picker with unique key
            predefined_colors = ["#00f900", "#ff5733", "#33c1ff", "#ff33a1", "#f0f0f0", "#1e1e1e"]
            selected_color = st.selectbox("Select a predefined color:", predefined_colors, index=0, key=f"predefined_color_{i + 1}")
            custom_color = st.color_picker("Or pick a custom color:", "#00f900", key=f"color_picker_{i + 1}")  # Unique key
            
            # Use the selected predefined color if chosen, otherwise use the custom color
            final_color = selected_color if selected_color else custom_color
            st.write(f"You picked: {final_color}")

            # New feature: Download button
            st.download_button(
                label="Download Image",
                data=img_url,
                file_name=f"car_image_{i + 1}.jpg",
                mime="image/jpeg"
            )

elif options == "About Us":
    st.header("About Us")
    st.write("We are dedicated to providing the best car services.")
    
    # New feature: Professional information
    st.subheader("Our Mission")
    st.write("Our mission is to deliver exceptional automotive services and products that exceed our customers' expectations.")
    
    st.subheader("Our Team")
    st.write("Our team consists of experienced professionals with a passion for cars and customer service. We have over 20 years of combined experience in the automotive industry.")
    
    st.subheader("Our Values")
    st.write("1. **Integrity**: We believe in honest and transparent dealings with our customers.\n"
             "2. **Quality**: We strive to provide the highest quality services and products.\n"
             "3. **Customer Satisfaction**: Our customers are our top priority, and we work hard to ensure their satisfaction.")

elif options == "Services":
    st.header("Our Services")
    st.write("We offer a variety of services including car sales, rentals, and maintenance.")
    
    # New feature: List of specific services
    st.subheader("Our Specific Services")
    services = {
        "Car Sales": "We provide a wide range of new and used cars at competitive prices.",
        "Car Rentals": "Rent a car for your needs, whether it's for a day or a month.",
        "Maintenance": "Regular maintenance services to keep your car in top condition.",
        "Car Financing": "Flexible financing options to help you purchase your dream car.",
        "Insurance Services": "We assist you in finding the best insurance for your vehicle."
    }
    
    for service, description in services.items():
        st.write(f"**{service}**: {description}")

elif options == "Contact":
    st.header("Contact Us")
    st.write("Feel free to reach out to us through our contact form.")
    
    # New feature: Contact form
    st.subheader("Get in Touch")
    
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    phone = st.text_input("Your Phone Number")
    message = st.text_area("Your Message")
    
    if st.button("Submit"):
        st.success("Thank you for your message! We will get back to you shortly.")
