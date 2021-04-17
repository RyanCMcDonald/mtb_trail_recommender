########## Run this code in your terminal to have it hosted on your browser! ##############  
########## In Terminal where file is saved: 'streamlit run 04_streamlit_code.py' ##########
########## Also hosted live @ https://rcm-mtb-trail.herokuapp.com/  #######################

################### IMPORTS ###################

import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import base64
from scipy import sparse
from sklearn.metrics.pairwise import pairwise_distances, cosine_similarity
from sklearn.preprocessing import MinMaxScaler
# @st.cache(suppress_st_warning=True)


################### SIDEBAR AND PAGE CONFIG ###################

st.set_page_config(
    page_icon='📖',
    initial_sidebar_state='expanded'   
) 
main_bg = "streamlit_background_1.jpg"
main_bg_ext = "jpg"

# setting backgroud of site
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# selections in drop-down menu on sidebar
page = st.sidebar.selectbox(
    'Page',
    ('Arizona/ Utah MTB Trails', 'Arizona Trail Recommender', 'Utah Trail Recommender')      
)


##################### PAGE 1 UTAH/ARIZONA TRAIL FILTER MAP #####################

# Page where user will filter out trails stats and choose which trail to enter into the recommender
if page == 'Arizona/ Utah MTB Trails':
    st.title('Arizona and Utah MTB Trails')   
    
    st.write('''
Whether you're a long-time resident to the area, or a first-time visitor, choosing which trail to ride can be a challenge!  Especially if you have no prior knowledge of the trails or don't know any locals within the riding area. Choosing the wrong trail could lead to a hazardous and unenjoyable ride, or even worse... injury. This page is dedicated to setting you off on the right foot! Below is a map containing all of the mountain bike trails within Arizona and Utah.  Each trail is represented on the map with a dot. Feel free to explore the interactive features of the map and narrow down the types of trails you'd be interested in riding.
    ''')

    st.write('''
Of course, trail ratings are relative to those who created them.  Only continue on trails you are comfortable riding and avoid putting yourself in situations above your abilities. Take caution when riding trails for the first time and don't forget the golden rule of mountain biking:
Pre-Ride, Re-Ride, Freeride! 

    ''')

    st.subheader('Mountain Bike Trail Filter')
    st.write('''
The map below can be used to filter out trails you’d like to ride.  Simply drag the selection bars or select options from the drop-down menus to adjust trail criteria. Once you have found a trail that suits you, enter it into the recommender systems on the next pages represented by the state in which your selected trail resides in.
    ''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1618607867884' style='position: relative'><noscript><a href='#'><img alt='az_ut_dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;S5&#47;S5TD8JZR7&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='ArizonaandUtahMTBTrails&#47;az_ut_dashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ar&#47;ArizonaandUtahMTBTrails&#47;az_ut_dashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1618607867884');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.minWidth='350px';vizElement.style.maxWidth='950px';vizElement.style.width='100%';vizElement.style.height='887px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 862, width= 740)   

    if __name__ == "__main__":
        main()
    
    
    st.subheader('Sedona, Arizona')
    st.write('''
One of the many amazing views in Arizona!
    ''') 

    st.image('./resources/sedona_pic.jpg', width=None)

################### PAGE 2 ARIZONA TRAIL RECOMMENDER ###################


elif page == 'Arizona Trail Recommender':
    st.title('Arizona Trail Recommender')
    st.subheader('So, which trail should you ride?')
    st.write('''
From the first page in the WebApp, select a trail you are interested in within Arizona. Enter it in the field below and we'll let you know the top ten trails you should try, based on your input. Or, select trail from searching [MTB Project](https://www.mtbproject.com/directory/8006911/arizona). Note, the recommender will not take routes.  And spelling counts!''')
    
    # when button pressed we check for input errors and start search
    az_trail_name = st.text_input('Enter target AZ trail name:').lower()
 
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

    #run recommender
    if az_trail_name:
    
    # need this result to reference the trail name index from az_rec and pull column data from az-trails (trail_dashboard)
        st.success('Most similar trails listed below below!')      
#         # display the similarity score of the rec trails
#         st.write(1-(az_rec[az_trail_name].sort_values().head(11)[1:]))
        
        st.write('''
Below are all of the trail stats, based on the recommended trails! ''')

        # reading in the stats data
        trail_stats = pd.read_csv('./data/trail_dashboard/az_trails.csv')    
    
        # assigning rec data (index) as a variable
        trails = az_rec[az_trail_name].sort_values().head(11).index
    
        # new variable with only rows form stats DF containing names in rec data
        stats = trail_stats[trail_stats['trail_name'].isin(trails)]
    
        # resetting index to trail name
        stats1 = stats.set_index('trail_name')
    
        # reindexing to match order of rec data
        stats2 = stats1.reindex(index=trails)
    
        # resetting index
        stats3 = stats2.reset_index()
        
        stats3 = stats3.set_index('trail_name')
    
        # writing to streamlit
        st.write(stats3)
        
        st.success('Shred Responsibly!  :sunglasses:')

    else:
        st.error('Please enter a valid trail name in box above')
        # error please input a target trail  
    

 ################### PAGE 3 UTAH TRAIL RECOMMENDER ###################
        
elif page == 'Utah Trail Recommender':
    st.title('Utah Trail Recommender')
    st.subheader('So, which trail should you ride?')
    st.write('''
From the first page in the WebApp, select a trail you are interested in within Utah. Enter it in the field below and we'll let you know the top ten trails you should try, based on your input. Or, select trail from searching [MTB Project](https://www.mtbproject.com/directory/8006911/arizona). Note, the recommender will not take routes.  And spelling counts!''')
    
   
    # when button pressed we check for input errors and start search
    ut_trail_name = st.text_input('Enter target UT trail name:').lower()
 
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
    

    #run recommender
    if ut_trail_name:
               
        st.success('Most similar trails listed below below!')

        st.write('''
Below are all of the trail stats, based on the recommended trails! ''')
        # reading in the stats data
        trail_stats_ut = pd.read_csv('./data/trail_dashboard/ut_trails.csv')    
    
        # assigning rec data (index) as a variable
        trails_ut = ut_rec[ut_trail_name].sort_values().head(11).index
 
        # new variable with only rows from stats DF containing names in rec data
        stats_ut = trail_stats_ut[trail_stats_ut['trail_name'].isin(trails_ut)]
    
        # resetting index to trail name
        stats_ut = stats_ut.set_index('trail_name')
    
        # reindexing to match order of rec data
        stats_ut = stats_ut.reindex(index=trails_ut)
    
        # resetting index
        stats_ut = stats_ut.reset_index()
        
        stats_ut = stats_ut.set_index('trail_name')
    
        # writing to streamlit
        st.write(stats_ut)
        
        st.success('Shred Responsibly!  :sunglasses:') 
    
    else:
        st.error('Please enter a valid trail name in box above')
        # error please input a target trail  