########## Run this code in your terminal to have it hosted on your browser!  In Terminal where file is saved: 'streamlit run 04_streamlit_code.py' ##########
########## Also hosted live @ https://food-ins-18.herokuapp.com/ ##########

## Code for embedding into in tableau from https://towardsdatascience.com/embedding-tableau-in-streamlit-a9ce290b932b
## Base code from streamlit lesson

import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from scipy import sparse
from sklearn.metrics.pairwise import pairwise_distances, cosine_similarity
from sklearn.preprocessing import MinMaxScaler
# @st.cache(suppress_st_warning=True)

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

    st.subheader('Mountain Bike Trail Filter')
    st.write('''
More kitty meow meow stuffs and things
    ''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1618359224445' style='position: relative'><noscript><a href='#'><img alt='az_ut_dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ar&#47;ArizonaandUtahMTBTrails&#47;az_ut_dashboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='ArizonaandUtahMTBTrails&#47;az_ut_dashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ar&#47;ArizonaandUtahMTBTrails&#47;az_ut_dashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1618359224445');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.minWidth='350px';vizElement.style.maxWidth='950px';vizElement.style.width='100%';vizElement.style.height='887px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 862, width= 740)   

    if __name__ == "__main__":
        main()
    
    
    st.subheader('Sedona, Arizona')
    st.write('''
One of the many amazing views in Arizona!
    ''') 

    st.image('./resources/sedona_pic.jpg', width=None)


elif page == 'Arizona Trail Recommender':
    st.title('Arizona Trail Recommender')
    st.subheader('So, which trail should you ride?')
    st.write('''
From the first page in the WebApp, select a trail you are interested in within Arizona. Enter it in the field below and we'll let you know the top ten trails you should try, based on your input. Or, select trail from [MTB Project](https://www.mtbproject.com/directory/8006911/arizona)''')
 
    # when button pressed we check for input errors and start search
    az_trail_name = st.text_input('Enter target AZ trail name:')
 
    # reading in the data
    az_trails = pd.read_csv('./data/recommender_data/az_trail_data.csv')
    
    # setting index
    az_trails = az_trails.set_index('trail_name')
    
    # creating the sparse matrix
    sparse_matrix = sparse.csr_matrix(az_trails.fillna(0))
       
    # calculating pairwise distances and building into a dataframe
    az_recs = pairwise_distances(sparse_matrix, metric = 'cosine')
    
    # saving pairwise matrix as a dataframe
    az_rec = pd.DataFrame(az_recs, index = az_trails.index, columns = az_trails.index)
    
   
    test = st.button('Search for recommended AZ trails')
  

    #run recommender
    if test:
               
        st.success('Most similar trails listed below below!')      
        st.write(1-(az_rec[az_trail_name].sort_values().head(11)[1:]))
        st.success('Go Shred!')

    else:
        st.error('Please enter a valid trail name in box above')
        # error please input a target trail  


elif page == 'Utah Trail Recommender':
    st.title('Utah Trail Recommender')
    st.subheader('So, which trail should you ride?')
    st.write('''
From the first page in the WebApp, select a trail you are interested in within Utah. Enter it in the field below and we'll let you know the top ten trails you should try, based on your input. Or, select trail from [MTB Project](https://www.mtbproject.com/directory/8010491/utah)''')

    # when button pressed we check for input errors and start search
    ut_trail_name = st.text_input('Enter target UT trail name:')
 
    # reading in the data
    ut_trails = pd.read_csv('./data/recommender_data/ut_trail_data.csv')
    
    # setting index
    ut_trails = ut_trails.set_index('trail_name')
    
    # creating the sparse matrix
    sparse_matrix = sparse.csr_matrix(ut_trails.fillna(0))
       
    # calculating pairwise distances and building into a dataframe
    ut_rec = pairwise_distances(sparse_matrix, metric = 'cosine')
    
    # saving pairwise matrix as a dataframe
    ut_rec = pd.DataFrame(ut_rec, index = ut_trails.index, columns = ut_trails.index)
    
    # return the dataframe
   
    test_1 = st.button('Search for recommended UT trails')
  

    #run recommender
    if test_1:
               
        st.success('Most similar trails listed below below!')
        
        # return top 10 trails in a dataframe
        st.write(1-(ut_rec[ut_trail_name].sort_values().head(11)[1:]))
        st.success('Go Shred!')

    else:
        st.error('Please enter a valid trail name in box above')
        # error please input a target trail  
         
        
        ##  Video embed code
#     with open("./resources/moab_video.mp4", 'rb') as v:
#         st.video(v)