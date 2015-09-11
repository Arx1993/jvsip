/* Created RJudd September 30, 2000 */
/* SPAWARYSCEN D857                 */
/**********************************************************************
// For TASP VSIPL Documentation and Code neither the United States    /
// Government, the United States Navy, nor any of their employees,    /
// makes any warranty, express or implied, including the warranties   /
// of merchantability and fitness for a particular purpose, or        /
// assumes any legal liability or responsibility for the accuracy,    /
// completeness, or usefulness of any information, apparatus,         /
// product, or process disclosed, or represents that its use would    /
// not infringe privately owned rights                                /
**********************************************************************/
/* $Id: vsip_tputoffset_l.c,v 2.0 2003/02/22 15:19:07 judd Exp $ */


#include"VI_support_priv_l.h"

vsip_tview_l* (vsip_tputoffset_l)(
  vsip_tview_l *v,
  vsip_offset o) {
    v->offset = o;
    return v;
}