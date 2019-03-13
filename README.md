# foundations
/****************************************************************************
2	**
3	** Copyright (C) 2017 Klaralvdalens Datakonsult AB (KDAB).
4	** Contact: http://www.qt-project.org/legal
5	**
6	** This file is part of the Qt3D module of the Qt Toolkit.
7	**
8	** $QT_BEGIN_LICENSE:LGPL3$
9	** Commercial License Usage
10	** Licensees holding valid commercial Qt licenses may use this file in
11	** accordance with the commercial license agreement provided with the
12	** Software or, alternatively, in accordance with the terms contained in
13	** a written agreement between you and The Qt Company. For licensing terms
14	** and conditions see http://www.qt.io/terms-conditions. For further
15	** information use the contact form at http://www.qt.io/contact-us.
16	**
17	** GNU Lesser General Public License Usage
18	** Alternatively, this file may be used under the terms of the GNU Lesser
19	** General Public License version 3 as published by the Free Software
20	** Foundation and appearing in the file LICENSE.LGPLv3 included in the
21	** packaging of this file. Please review the following information to
22	** ensure the GNU Lesser General Public License version 3 requirements
23	** will be met: https://www.gnu.org/licenses/lgpl.html.
24	**
25	** GNU General Public License Usage
26	** Alternatively, this file may be used under the terms of the GNU
27	** General Public License version 2.0 or later as published by the Free
28	** Software Foundation and appearing in the file LICENSE.GPL included in
29	** the packaging of this file. Please review the following information to
30	** ensure the GNU General Public License version 2.0 requirements will be
31	** met: http://www.gnu.org/licenses/gpl-2.0.html.
32	**
33	** $QT_END_LICENSE$
34	**
35	****************************************************************************/
36	
37	#include "qclock.h"
38	#include "qclock_p.h"
39	#include <Qt3DCore/qpropertyupdatedchange.h>
40	
41	QT_BEGIN_NAMESPACE
42	
43	namespace Qt3DAnimation {
44	
45	QClockPrivate::QClockPrivate()
46	    : Qt3DCore::QNodePrivate()
47	    , m_playbackRate(1.0f)
48	{
49	}
50	
51	QClock::QClock(Qt3DCore::QNode* parent)
52	    : Qt3DCore::QNode(*new QClockPrivate, parent)
53	{
54	}
55	
56	QClock::QClock(QClockPrivate &dd, Qt3DCore::QNode *parent)
57	    : Qt3DCore::QNode(dd, parent)
58	{
59	}
60	
61	QClock::~QClock()
62	{
63	}
64	/*!
65	    \property Qt3DAnimation::QClock::playbackRate
66	
67	    The playback speed of the animation.
68	*/
69	
70	double QClock::playbackRate() const
71	{
72	    Q_D(const QClock);
73	    return d->m_playbackRate;
74	}
75	
76	void QClock::setPlaybackRate(double playbackRate)
77	{
78	    Q_D(QClock);
79	    if (qFuzzyCompare(playbackRate, d->m_playbackRate))
80	        return;
81	    d->m_playbackRate = playbackRate;
82	    emit playbackRateChanged(playbackRate);
83	}
84	
85	Qt3DCore::QNodeCreatedChangeBasePtr QClock::createNodeCreationChange() const
86	{
87	    auto creationChange = Qt3DCore::QNodeCreatedChangePtr<QClockData>::create(this);
88	    auto &data = creationChange->data;
89	    Q_D(const QClock);
90	    data.playbackRate = d->m_playbackRate;
91	    return creationChange;
92	}
93	
94	}
95	
96	QT_END_NAMESPACE
