import streamlit as st

# Set page title and configuration
st.set_page_config(page_title="USA States List", page_icon="🗺️")

# List of all 50 USA states
usa_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California",
    "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

# Streamlit UI
def main():
    st.title("🗺️ USA States List")
    st.write("A comprehensive list of all 50 states in the United States of America")
    
    # Display total count
    st.metric(label="Total States", value=len(usa_states))
    
    st.divider()
    
    # Search functionality
    st.subheader("🔍 Search States")
    search_term = st.text_input("Enter state name to search:", "")
    
    if search_term:
        filtered_states = [state for state in usa_states if search_term.lower() in state.lower()]
        st.info(f"Found {len(filtered_states)} state(s) matching '{search_term}'")
        
        if filtered_states:
            for state in filtered_states:
                st.write(f"• {state}")
        else:
            st.warning("No states found matching your search.")
    else:
        # Display all states
        st.subheader("📋 All States (Alphabetically)")
        
        # Display in columns for better layout
        col1, col2, col3 = st.columns(3)
        
        # Divide states into three columns
        states_per_column = len(usa_states) // 3 + 1
        
        with col1:
            for state in usa_states[:17]:
                st.write(f"• {state}")
        
        with col2:
            for state in usa_states[17:34]:
                st.write(f"• {state}")
        
        with col3:
            for state in usa_states[34:]:
                st.write(f"• {state}")
    
    st.divider()
    
    # Additional information
    st.info("ℹ️ The United States consists of 50 states, each with its own government and laws.")
    
    # Fun fact expander
    with st.expander("📚 Fun Facts about USA States"):
        st.write("**Largest State by Area:** Alaska (665,384 sq mi)")
        st.write("**Smallest State by Area:** Rhode Island (1,214 sq mi)")
        st.write("**Most Populous State:** California (approximately 39 million)")
        st.write("**Least Populous State:** Wyoming (approximately 580,000)")
        st.write("**Newest States:** Alaska and Hawaii (both admitted in 1959)")

# Run the app
if __name__ == "__main__":
    main()
