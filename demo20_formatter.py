# encoding=UTF-8
print '==%10s==' % ('0123456789')
print '==%10s==' % ('01234')
print '==%-10s==' % ('01234')
print '==%*s==' % (-10, '01234')
print '==%*s==' % (10, '01234')
print '=={:<10s}=='.format('01234')
print '=={:>10s}=='.format('01234')
print '=={:<{}s}=='.format('01234', 10)
print '=={:>{}s}=='.format('01234', 10)
"""
=======我只是一個分隔線============
"""
# encoding=UTF-8
print '==%10s==' % ('0123456789')
print '==%10s==' % ('01234')
print '=={:10s}=='.format('01234')
print '=={:#<10s}=='.format('01234')
print '=={:.>10s}=='.format('01234')
print '=={:"^10s}=='.format('01234')
print '%.6f' % (3.1415926837)
print '%.6s' % ('hello_world')
print '%.6s' % ('可以使用中文的方式')
print '%.6s' % (u'可以使用中文的方式')
print '{:.6s}'.format('可以使用中文的方式')
print u'{:.6s}'.format(u'可以使用中文的方式')
print '{:.{}s}'.format('可以使用中文的方式', 6)
print '%.*s' % (6,u'可以使用中文的方式')