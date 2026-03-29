import os
import requests
from PIL import Image
from io import BytesIO

# 圖片清單
images = [
    {"id": "1VMTMZk8svuXWXUZK6k3o0CCPosynhd3I", "name": "臺北體育園區1"},
    {"id": "1n5qCx85ZBVNm4SPFW4qphoHnZOv7ux8H", "name": "臺北體育園區2"},
    {"id": "1Eg9vDMFyLNaNjSYy8KjHW107MZFL7GvX", "name": "臺北市政府1"},
    {"id": "1Is-snQeK7nO2G-LRfKUwuE7N_J8FkVCu", "name": "臺北市政府2"},
    {"id": "1Jbxjzl9Y8DcFwUOu2J8mmAfspOGmg6Pj", "name": "大巨蛋文化體育園區1號"},
    {"id": "1yL8NzYo0Ava_v-WLz3yuh8Rgu4uhJ8zo", "name": "大巨蛋文化體育園區2號"},
    {"id": "1LnbUQ---qdygz2Lq3d4ug1kcVhILUszA", "name": "大巨蛋文化體育園區3號"},
    {"id": "11EMkyEloZszy3VfkIMsHn6vD0L7EmUvy", "name": "大巨蛋文化體育園區4號"},
    {"id": "1h6A6vg-dre7NcjDN57vpA6AL4ddf0Gf1", "name": "大巨蛋文化體育園區5號"},
    {"id": "11lq71qGJzVVEdw71XW7yfQYNuqBpDrD6", "name": "大巨蛋文化體育園區6號"},
    {"id": "1LvtGVzwwy5VjCd1sgHH5GOXUY86lFZ1B", "name": "臺北市懷愛館火化場旁"},
    {"id": "1i7HjmRBmY-1xoJe4YIJr96wa1dj2dFzB", "name": "臺北市懷愛館停柩室廁所外"},
    {"id": "16xHyBM6JYYj6ItKRw1dIhz5kR1NE4Afr", "name": "臺北市懷愛館景仰樓2樓露臺"},
    {"id": "1pm3zRVhbYvk1ATjeWwApDVHLnhp7tXIa", "name": "臺北市懷愛館中庭景行樓室外梯下方"},
    {"id": "1fD7MX8AfAE8YCg8YASOroIOAot1TuF8z", "name": "臺北市懷愛館景行樓4樓園圃"},
    {"id": "1mpI4NQyx_mNcvuJk8DfOCUHMEU3LC1nE", "name": "臺北市懷愛館計程車停等區"},
    {"id": "1aU8vsEwm3psDhArS7_Skh-mnAFjM7B8J", "name": "臺北市萬華區公所"},
    {"id": "1rYz3AZW23ue3JyYRjZVUE_MSv-08F_iT", "name": "臺北市文山區公所"},
    {"id": "14_qIQD7HZCQu48pTGVo5C4HwH1DlAS_j", "name": "台北南港展覽館1館南側"},
    {"id": "1RXALvoRkBw388Nro72j4V-3pSoKt-Szs", "name": "台北南港展覽館1館東側"},
    {"id": "1WJCYnfemif3A6vPSMa8RP9RG9Md_4CLa", "name": "台北南港展覽館2館1"},
    {"id": "1ycYtCXp-d-mYex79vFWxKXys8YCjPLQb", "name": "台北南港展覽館2館2"},
    {"id": "1w9WWrVgX-6RdSammLlFqvYBSwOat55lD", "name": "台北南港展覽館2館3"},
    {"id": "1apPyrPSxB3t-UHv9IJZmEG0jbbaZ9oeM", "name": "臺北市士林區公所"},
    {"id": "17ByX2Ej1LOLKKuL6yabinbrgG6OsYgq3", "name": "陽明山國家公園-冷水坑遊憩區"},
    {"id": "1gSVxpw-d1OIwlw-1FJ9pVcfpOKnMahOY", "name": "陽明山國家公園-擎天崗草原景觀區"},
    {"id": "1tl2TwdTxIpvP1LHZk5kOg0EHaCkmvjMW", "name": "陽明山國家公園-天溪園生態教育中心"},
    {"id": "1BoujAXJ-8-cMKvd_JZPelh6YJqoNI7T8", "name": "陽明山國家公園-菁山自然中心"},
    {"id": "1gHYh9CM8X0Xw_KTF-0exii05MpP1pmzk", "name": "陽明山國家公園-小油坑遊憩區"},
    {"id": "140b6M2er6-4XPsHjj2_9Ce7PhqV6T5EL", "name": "陽明山國家公園-遊客中心"},
    {"id": "1TO1gNqWgD19-D0_LzTrQE8cAYQkK3hgG", "name": "陽明山國家公園-管服中心1"},
    {"id": "10-D4DIvbh56mQA1exgBX70EM1X86KUqu", "name": "陽明山國家公園-管服中心2"},
    {"id": "17bau5oz5DEarzBJ0Tytjq_5EvOQG-jpn", "name": "陽明山國家公園-陽明書屋"},
    {"id": "1fWUpWVrOPMeOt0uc3cROl_7T0MO7MNNJ", "name": "陽明山國家公園-龍鳳谷遊憩區"},
    {"id": "1mM68-ReNRmlcF0RauqEokN5wZLK2hEik", "name": "國立故宮博物院第一展覽館"},
    {"id": "1e5w2BRQ_fxrZm7Fc6wytynQCtN9sejEe", "name": "國立故宮博物院第一展覽館西側"},
    {"id": "15U4hBU1N1n6KEOoXZ2m_cdl2VTxFeR0D", "name": "國立故宮博物院研究大樓"},
    {"id": "16gGy-COuCWsbTw0UIIO-66VasrM429aP", "name": "Place 享．信義(僅供加熱菸使用)"},
    {"id": "1uBXUVOZ_QUG15F249BMY3-2PjVYpB247", "name": "Place 享．敦南(僅供加熱菸使用)"},
    {"id": "1m-GDl5bIMqfRpZzysMKkFnSTSavavd7j", "name": "Q-store 民權店(僅供合法加熱菸使用)"},
    {"id": "1GyD-2p1IQ7z-TnrVwjboul3Chwz1A1zX", "name": "Mitsui Shopping Park LaLaport 南港"},
    {"id": "13PsRkd7p8NvmhsmnROlYTaWKttKeJ_UC", "name": "台北晶華酒店"}
]

save_dir = "smoking_area_jpgs"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

print(f"開始下載並轉換圖片至 {save_dir}...")

for img_info in images:
    url = f"https://drive.google.com/uc?export=download&id={img_info['id']}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # 使用 PIL 讀取二進位資料
            img = Image.open(BytesIO(response.content))
            
            # 如果圖片有透明層 (RGBA)，轉換為 RGB 才能存成 JPG
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # 強制存成 .jpg
            target_name = f"{img_info['name']}.jpg"
            save_path = os.path.join(save_dir, target_name)
            
            img.save(save_path, "JPEG", quality=90)
            print(f"成功處理: {target_name}")
        else:
            print(f"下載失敗: {img_info['name']} (HTTP {response.status_code})")
    except Exception as e:
        print(f"處理 {img_info['name']} 時發生錯誤: {e}")

print("任務完成！")