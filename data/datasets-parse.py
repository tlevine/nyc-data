#!/usr/bin/env python2
import os
import lxml.html

DIR = os.path.join('downloads', 'datasets')

def main():
    pages = filter(lambda page: '.html' == page[-5:], os.listdir(DIR))
    viewids = set()
    for page in pages:
        html = lxml.html.parse(os.path.join(DIR, page))
        viewids = viewids.union(parse(html))
    print ' '.join(viewids)

def parse(html):
    'Get the viewids out.'
    return set(map(unicode, html.xpath('//tr[@itemtype="http://schema.org/Dataset"]/@data-viewid')))

#<tr itemscope="itemscope" itemtype="http://schema.org/Dataset" class="item collapsed  local" data-viewid="yc6c-pk2a">
#                    <td class="index" scope="row">
#                                          <a class="expander collapsed" title="Click to expand" href="#Expand">
#                                                                  <span class="icon"></span>
#                                                                                        </a>
#                                                                                                              <span class="value">761.</span>
#                                                                                                                                  </td>
#
#
#
#                                                                                                                                                      <td class="nameDesc">
#                                                                                                                                                                            <span class="hide" itemprop="name">Directory of City Resources</span>
#                                                                                                                                                                                                  <a itemprop="url" href="/Social-Services/Directory-of-City-Resources/yc6c-pk2a" class="name" rel="">Directory of City Resources</a>
#                                                                                                                                                                                                                        <span class="category infoItem">Social Services</span>
#                                                                                                                                                                                                                                              <span class="tags infoItem" itemprop="keywords">ocdv, combat, domestic violence, jobs, ...</span>
#
#                                                                                                                                                                                                                                                                    <div class="expandBlock clearfix collapsed">
#                                                                                                                                                                                                                                                                                            <div class="description">List of resources that address the domestic violence issues</div>
#                                                                                                                                                                                                                                                                                                                    <div class="rowSearchResults"></div>
#                                                                                                                                                                                                                                                                                                                                            <div class="extraInfo ">
#                                                                                                                                                                                                                                                                                                                                                                      <div class="infoContent"></div>
#                                                                                                                                                                                                                                                                                                                                                                                                <a class="close collapsed" href="#Close"><span class="icon"></span></a>
#                                                                                                                                                                                                                                                                                                                                                                                                                        </div>
#                                                                                                                                                                                                                                                                                                                                                                                                                                              </div>
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                  </td>
#
#
#
#
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      <td class="popularity">
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            <span
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            class="visits">8
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            views</span>
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </td>
#
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <td
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    class="type
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    typeBlist"
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    title="Table">
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          <a
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          href="/Social-Services/Directory-of-City-Resources/yc6c-pk2a"
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          rel=""><div
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          class="icon"></div></a>
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              </td>
#
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </tr>


if __name__ == '__main__':
    main()