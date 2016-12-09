constant_vals = ()
constant_vals = (39,)
constant_vals = ()
constant_vals = (39,)

print type(constant_vals)
constant_vals = ("Jack","Arizona",9,"Atlanta",9,14,6)
print len(constant_vals)
print constant_vals.count(9)

#Sets

linux_essentials = set(["John", "Kevin","Anthony","James", "Sara", "Marge","John"])
lpic_level1 = set(["Kevin", "James", "Marge","Lewis", "Nancy"])

both_courses = linux_essentials & lpic_level1
print "Took both %s" %(both_courses)

need_to_watch_le = lpic_level1 - linux_essentials

print "need to watch = "+str(need_to_watch_le)
