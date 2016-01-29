#ignore thresholds
im = mpl.image.imread('FRAME_initial demag_3.4 ps_500 Hz_2_29_AVR.png')
figure()
imshow(im)
mean(im[300:323, 200:490])
im[300:323, 200:490]
im[300:323, 200:490].flatten()
hist(im[300:323, 200:490].flatten())
figure()
hist(im[300:323, 200:490].flatten())
hist(im[300:323, 200:490].flatten(), bins=100)
hist(im[300:323, 200:490].flatten(), bins=20)
cla()
imshow(im)
figure()
for x in linspace(200, 350, 10):
    hist(im[x:x+25, 200:490].flatten())
cla()
figure()
for x in linspace(200, 350, 10):
    hist(im[x:x+25, 200:490].flatten(), alpha=.3, bins=20)
figure()
dataset = []
location = []
for x in linspace(200, 350, 10):
    dataset.append(im[x:x+25, 200:490].flatten())
    location.append(x)
violinplot(dataset, location)
#ce(200, 350, 10):
#  if self._edgecolors == str('face'):

#    dataset.append(im[x:x+25, 200:490].flatten())
#    location.append(x)
violinplot(dataset, location, widths=25)
figure()
dataset = []
location = []
for x in linspace(200, 350, 10):
    dataset.append(im[x:x+25, 200:490].flatten())
    location.append(x)
violinplot(dataset, location, widths=25)
figure()
dataset = []
location = []
for x in arange(0, 700, 25):
    dataset.append(im[x:x+25, 200:490].flatten())
    location.append(x)
violinplot(dataset, location, widths=25)
figure()
dataset = []
location = []
for x in arange(0, 700, 15):
    dataset.append(im[x:x+25, 200:490].flatten())
    location.append(x)
violinplot(dataset, location, widths=25)
plot( location,[mean(v) for v in dataset])
mdata =[mean(v) for v in dataset]
bgdata = concatenate((mdata[82:145], mdata[203:278], mdata[334:387], mdata[435:457], mdata[501:532], mdata[570:]))
xdata = concatenate((range(82,145), range(203,278), range(334,387), range(435,457), range(501,532), (570,)))
#poly = polyfit(xdata, bgdata, 4)
figure()
dataset = []
location = []
for x in range(len(im)):
    dataset.append(im[x:x+1, 200:490].flatten())
    location.append(x)
mdata =[mean(v) for v in dataset]
figure()
plot( location,[mean(v) for v in dataset])
bgdata = concatenate((mdata[82:145], mdata[203:278], mdata[334:387], mdata[435:457], mdata[501:532], mdata[570:]))
xdata = concatenate((range(82,145), range(203,278), range(334,387), range(435,457), range(501,532), (570,len(im))))
bgdata = concatenate((mdata[82:145], mdata[203:278], mdata[334:387], mdata[435:457], mdata[501:532], mdata[570:]))
xdata = concatenate((range(82,145), range(203,278), range(334,387), range(435,457), range(501,532), range(570,len(im))))
poly = polyfit(xdata, bgdata, 4)
plot(xdata, polyval(poly, xdata))
figure()
h = len(im)
h
plot(mdata - polyval(poly, range(h)))
figure()
bg = polyval(poly, range(h))
bg.T
hstack([bg]*len(im[0]))
vstack([bg]*len(im[0]))
imshow(vstack([bg]*len(im[0])))
imshow(vstack([bg]*len(im[0])).transpose())
imshow(im[0])
imshow(im[:,:,0] - vstack([bg]*len(im[0])).transpose())
imshow(vstack([bg]*len(im[0])).transpose())
colorbar()
imshow(im[:,:,0] - vstack([bg]*len(im[0])).transpose(), cmap='Greys')
colorbar()
