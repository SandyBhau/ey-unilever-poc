# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    st.set_page_config(
        page_title="EY_Streamlit",
        page_icon="👋",
    )

    st.write("# EY to Streamlit Demo! 👋")
    
    df = pd.DataFrame(
    [
        {"EY Operations": "Gen AI Solutions", "Project Implementaion": 20, "Download Project Impact": True},
        {"EY Operations": "Data Science", "Project Implementaion": 50, "Download Project Impact": True},
        {"EY Operations": "Machine Learning", "Project Implementaion": 40, "Download Project Impact": True},
    ]
    )
    prompt = st.chat_input("Say something")

    csv = convert_df(df)

    st.dataframe(df, use_container_width=True)
    st.bar_chart(data=df,  x="EY Operations", y="Project Implementaion",  color=None, width=0, height=0, use_container_width=True)
    st.download_button(label= "Download Project Impact", data=csv, file_name='Project_Impact.csv',mime='text/csv')
    if prompt:
      st.write(f"User has sent the following prompt: {prompt} {LOGGER}")

    # st.sidebar.success("Select a demo above.")

    # st.markdown(
    #     """
    #     Streamlit is an open-source app framework built specifically for
    #     Machine Learning and Data Science projects.
    #     **👈 Select a demo from the sidebar** to see some examples
    #     of what Streamlit can do!
    #     ### Want to learn more?
    #     - Check out [streamlit.io](https://streamlit.io)
    #     - Jump into our [documentation](https://docs.streamlit.io)
    #     - Ask a question in our [community
    #       forums](https://discuss.streamlit.io)
    #     ### See more complex demos
    #     - Use a neural net to [analyze the Udacity Self-driving Car Image
    #       Dataset](https://github.com/streamlit/demo-self-driving)
    #     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    # """
    # )


if __name__ == "__main__":
    run()
