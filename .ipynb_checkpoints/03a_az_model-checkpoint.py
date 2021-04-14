########## Run this code in your terminal to have it hosted on your browser!  In Terminal where file is saved: 'streamlit run 04_streamlit_code.py' ##########
########## Also hosted live @ https://food-ins-18.herokuapp.com/ ##########

## Code for embedding into in tableau from https://towardsdatascience.com/embedding-tableau-in-streamlit-a9ce290b932b
## Base code from streamlit lesson

import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st




st.set_page_config(
    page_icon='📖',
    initial_sidebar_state='expanded'
    

)
  
page = st.sidebar.selectbox(
    'Page',
    ('Arizona/ Utah MTB Trails', 'Arizona Trail Recommender', 'Utah Trail Recommender')   
    
)


if page == 'Arizona/ Utah MTB Trails':
    st.title('Arizona and Utah MTB Trails')  
    
    
    st.write('''
Soft kitty warm kitty little ball of furr sleep but chase mice, so destroy the blinds. Nap all day have my breakfast spaghetti yarn stare at guinea pigs or weigh eight pounds but take up a full-size bed pee in human's bed until he cleans the litter box yet side-eyes your "jerk" other hand while being petted . Lick plastic bags nyan fluffness ahh cucumber!. Make it to the carpet before i vomit mmmmmm jump on human and sleep on her all night long be long in the bed, purr in the morning and then give a bite to every human around for not waking up request food, purr loud scratch the walls, the floor, the windows, the humans, play time, for furball roll roll roll car rides are evil. Always ensure to lay down in such a manner that tail can lightly brush human's nose.
    ''')

    st.write('''
Blow up sofa in 3 seconds love fish for jump on human and sleep on her all night long be long in the bed, purr in the morning and then give a bite to every human around for not waking up request food, purr loud scratch the walls, the floor, the windows, the humans so rub butt on table yet lick master's hand at first then bite because im moody so ignore the human until she needs to get up, then climb on her lap and sprawl, to pet a cat, rub its belly, endure blood and agony,
    ''')

    st.subheader('Mountain Bike trail Filter')
    st.write('''
More kitty meow meow stuffs and things
    ''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1618184133668' style='position: left'><noscript><a href='#'><img alt='az_ut_dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ar&#47;ArizonaandUtahMTBTrails&#47;az_ut_dashboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='ArizonaandUtahMTBTrails&#47;az_ut_dashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ar&#47;ArizonaandUtahMTBTrails&#47;az_ut_dashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1618184133668');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.minWidth='350px';vizElement.style.maxWidth='950px';vizElement.style.width='100%';vizElement.style.height='887px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 868, width= 740)   

    if __name__ == "__main__":
        main()
    
    
    st.subheader('Sedona, Arizona')
    st.write('''
One of the many amazing views in Arizona!
    ''') 

    st.image('./resources/sedona_pic.jpg', width=None)
    
##  Video embed code
#     with open("./resources/moab_video.mp4", 'rb') as v:
#         st.video(v)


elif page == 'Arizona Trail Recommender':
    st.title('Arizona Trail Recommender')
    st.subheader('So, which trail should you ride?')
    st.write('''
From the first page in the WebApp, select a trail you are interested in within Arizona. Enter it in the field below and we'll let you know the top ten trails you should try, based on your input.''')

    # enter the trail name you've choosen
    az_trail_name = st.text_input('Enter target trail name:')
    
    test = st.button('Search for recommended trails')
    
    # returning the results in a dataframe
    st.dataframe(models.az_trail_rec(target_id=az_trail_name))
    
    # tell the user when the results are completed
    st.success('Get out and ride!') 
    
elif page == 'Utah Trail Recommender':
    st.title('Something Else')
    st.subheader('Socioeconomic factors associated with Food Insecurity')
    st.write('''
A variety of factors contribute to food insecurity in a given community. Factors such as income, employment, access to healthcare, and education are just a few factors at play in affecting one's access to food. The below visualizations depict Food Insecurity vs. formal education for each state in the overlying map with median household income depicted in the bar graph below.
    ''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616974092017' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;St&#47;State_Based_FI_Rate&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='State_Based_FI_Rate&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;St&#47;State_Based_FI_Rate&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1616974092017');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.minWidth='420px';vizElement.style.maxWidth='1020px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='787px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 1000, width = 900)
    if __name__ == "__main__":
        main()


