import streamlit as st
import pandas as pd
import pydeck as pdk

# 위도, 경도 데이터 준비
data = pd.DataFrame({
    'city': ['Los Angeles'],
    'lat': [34.0522],
    'lon': [-118.2437],
    'population': [3800000]    
})

st.title("가보고 싶은 장소")
st.map(data)

# 3. Pydeck Chart
st.subheader("PyDeck Chart (st.pydeck_chart)")
layer = pdk.Layer(
    "ScatterplotLayer",  #점(원형 마커)을 표시
    data=data,
    get_position="[lon, lat]",
    get_radius=5000,  #점(원의 반지름)을 미터 단위로 지정. 5000이면 지상에서 약 5km 반경의 원으로 보임
    get_color=[255, 0, 0],
    pickable=True  #마우스로 점을 클릭했을 때 툴팁(정보창) 을 표시
)

# 툴팁 설정
tooltip = {
    "text": "도시: {city}\n인구: {population}",
    "style": {"color": "white"}
}

# 대한민국 전체가 보이는 위치로 설정
view_state = pdk.ViewState(
    latitude=34.0,  #지도의 중심 위도(lat), 36.5는 한반도의 대략적인 중앙 위도
    longitude=-118.3, #지도의 중심 경도(lon), 127.8은 한국의 대략적인 중앙 경도
    zoom=6,
    pitch=0  # 지도를 기울이는 각도 0은 정면
)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip=tooltip))
