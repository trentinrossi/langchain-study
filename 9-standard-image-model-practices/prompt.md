# Style modifiers
golden gate bridge in the style of surrealism

# Quality boosters
golden gate bridge in the style of a high resolution photo

# Negative prompts
peppa pig --no cartoon

# Weighted terms
golden gate bridge:: by van gogh::0.9, by picasso::0.1 clouds::-1

# Rewrite prompt
Rewrite this prompt for DALL-E with meticulous art direction and descriptive words. You should aim to generate an image true to this artist's medium. No need to say "create an image" just describe the composition:

# Inpainting (Change and adjust the current image)
photograph of a beautiful 1920s flapper girl at a party, nice smile, wide angle, in color, 3 5 mm, dslr

# Outpainting (Generate a new image based on the current image)
photograph of 2 beautiful 1920s flapper girls at a party, nice smile, wide angle, in color, 3 5 mm, dslr
photograph of glamorous woman in a 1920s flapper party, wearing a sequin dress, wide angle, in color, 3 5 mm, dslr

# Character prompt
two images side by side, rockstar American rough and ready middle-age jawline actor man, photo booth portrait --ar 2:1

side profile image, rockstar American rough and ready middle-age jawline actor man, photo booth portrait --ar 2:1

# Migrating to Stable Diffusion XL in AUTOMATIC1111
prompt:
anime cat girl with pink hair and a cat ears outfit is posing for a picture in front of a gaze, photorealistic, 1girl, a character portrait, floral print, Alice Prin, sots art, official art, sunlight, wavy hair, looking at viewer

negative:
disfigured, ugly, bad, immature, photo, amateur, overexposed, underexposed

seed:
3588970703

models:
https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/tree/main
https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/tree/main