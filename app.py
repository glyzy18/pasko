import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Set up page configuration with a Christmas theme
st.set_page_config(page_title="My Christmas Celebration", page_icon="🎄", layout="wide")

# Lottie animation function
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()






# ---- HEADER SECTION ----
with st.container():
    st.subheader("Ho Ho Ho! 🎅 I'm Glyza M. Pagambunan")
    st.title("Celebrating Christmas with Joy and Cheer")
    st.write("The Christmas season is here! Let's spread some festive cheer and celebrate the most wonderful time of the year! 🎄")

st.title("Merry Christmas and Happy Holidays! 🎄✨")
st.subheader("Let’s Make This Christmas Special with Joy and Festive Cheer! 🎅")

# Lottie animation for Christmas welcome message
lottie_url = "https://assets8.lottiefiles.com/packages/lf20_1lhjm5er.json" 
lottie_animation = load_lottie_url(lottie_url)
if lottie_animation:
    st_lottie(lottie_animation, speed=1, width=700, height=400, key="welcome")

# Introduction
st.markdown("""
Welcome to my *Christmas Celebration!* 🎉  
This season is all about love, joy, and togetherness. Whether you're planning a cozy holiday gathering, exchanging gifts, or enjoying the festive lights, Christmas brings people together. Let's explore some fun ways to make this Christmas unforgettable!
""")

# Festive Ideas Section

st.markdown("""
## 🎄 Fun Ideas to Celebrate Christmas

Christmas is the perfect time to create lasting memories with loved ones. Here are some fun ideas to make your holiday celebration even more magical:

### 1. 🎁 *Gift-Giving with a Personal Touch*

The best gifts are the ones that come from the heart. Whether it's a DIY gift or something you know they’ll love, a thoughtful present shows you care. Try making your own Christmas cards, or personalize gifts for that extra touch of love. 

**Idea**: Create a holiday gift guide with unique, personalized gifts for friends and family—maybe even organize a Secret Santa exchange to add more fun!

### 2. 🎅 *Christmas Movie Marathon*

Gather the family and friends for a cozy Christmas movie marathon! Whether it’s classics like *Home Alone*, *The Grinch*, or newer hits like *Klaus*, Christmas movies are the perfect way to spread festive cheer.

**Pro Tip**: Make it a potluck movie night! Everyone can bring a Christmas treat (like gingerbread cookies or hot chocolate) to share as you watch the films.

### 3. 🌟 *Decorate Your Home with Holiday Spirit*

Transform your home into a winter wonderland by decorating with Christmas lights, a tree, and beautiful ornaments. Don’t forget about the outside—string up lights around your porch or windows to spread the Christmas cheer to your neighborhood!

**Creative Tip**: Host a "decorate the house" competition with your family. See who can make the most creative Christmas decoration!

### 4. 🍪 *Bake Christmas Treats*

What’s Christmas without baking? Get your oven going and bake some Christmas treats like sugar cookies, gingerbread men, or a Yule log cake. Baking together is a fun and festive way to bond with family and friends.

**Holiday Tip**: Set up a Christmas cookie decorating station and invite loved ones to decorate their cookies with frosting, sprinkles, and candy!

### 5. 🤶 *Volunteer and Spread the Joy*

Christmas is a time for giving, and what better way to embrace the holiday spirit than by giving back? Volunteer at a local shelter, donate clothes, or help wrap gifts for those in need. It’s the season of kindness and generosity.

**Tip**: Organize a community gift drive or a volunteer event to bring some joy to those who need it the most!

---

## 🌟 Bonus Christmas Fun

- *Christmas Caroling* 🎤  
  Get into the Christmas spirit by singing your favorite holiday carols with friends or family. You can even organize a caroling event for your neighborhood!

- *Holiday Games* 🎉  
  Play fun holiday games like Christmas trivia, a Christmas scavenger hunt, or Pin the Nose on Rudolph. Games are a great way to create laughter and joy.

- *Christmas Lights Tour* 🌟  
  Take a walk or drive around your neighborhood to see the Christmas lights. Make it a tradition to admire all the beautiful decorations and festive displays.

## 💡 Conclusion

Christmas is a time to cherish the little moments, be with the people you love, and spread joy wherever you go. From decorating your home to sharing festive meals and gifts, there are endless ways to make this Christmas one to remember. 🎄

Let’s fill the season with love, kindness, and festive cheer. Merry Christmas and a Happy New Year to all! 🎅🎉
""")

# Lottie animation for Christmas conclusion
lottie_url_end = "https://assets8.lottiefiles.com/packages/lf20_rikjpqjf.json"  # Lottie animation for Christmas conclusion (can be replaced)
lottie_animation_end = load_lottie_url(lottie_url_end)
if lottie_animation_end:
    st_lottie(lottie_animation_end, speed=1, width=700, height=400, key="conclusion")

st.markdown("---")

st.markdown("""
*Thanks for celebrating Christmas with me!* 🎅🎄  
If you have any fun Christmas ideas, want to share your holiday traditions, or simply want to wish everyone a Merry Christmas, feel free to leave a comment! Let’s keep spreading holiday cheer and make this season unforgettable! 🎁🎉
""")
