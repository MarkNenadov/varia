/* KvtmlVocabularyParser
 *
 * Mark J. Nenadov (2014)
 * Essex, Ontario
 * Email: <marknenadov@gmail.com>
 *
 * LICENSING
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version
 *
 * This program is distributed in the hope that it will be useful
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 *
 */

package com.pythonbyte.util.parser;

import com.pythonbyte.domain.VocabularyEntry;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class KvtmlVocabularyParser {
    private Document document;

    /* Constructors */
    public KvtmlVocabularyParser(Document document) {
        this.document = document;
    }

    /* Services */
    public List<VocabularyEntry> getVocabularyEntries() {
        List<VocabularyEntry> vocabularyEntries = new ArrayList<>();
        for (Node entriesNode : getChildNodesFromNodeList(document.getFirstChild().getChildNodes(), "entries")) {
            for (Node entryNode : getChildNodesFromNodeList(entriesNode.getChildNodes())) {
                addTranslationToVocabularyEntryList(getChildNodesFromNodeList(entryNode.getChildNodes(), "translation"), vocabularyEntries);
            }
        }

        return vocabularyEntries;
    }

    /* Helpers */
    private void addTranslationToVocabularyEntryList(List<Node> translationNodes, List<VocabularyEntry> vocabularyEntries) {
        VocabularyEntry vocabularyEntry = new VocabularyEntry();
        if (translationNodes.size() == 2) {
            List<Node> textNodes = getChildNodesFromNodeList(translationNodes.get(0).getChildNodes(), "text");

            if (textNodes.size() == 1) {
                vocabularyEntry.setWord(textNodes.get(0).getTextContent());
            }
            textNodes = getChildNodesFromNodeList(translationNodes.get(1).getChildNodes(), "text");

            if (textNodes.size() == 1) {
                vocabularyEntry.setTranslation(textNodes.get(0).getTextContent());
            }
            vocabularyEntries.add(vocabularyEntry);
        }
    }

    private List<Node> getChildNodesFromNodeList(NodeList nodeList) {
        List<Node> nodes = new ArrayList<>();

        for ( int i=0; i<nodeList.getLength(); i++) {
            nodes.add( nodeList.item( i ) );
        }

        return nodes;
    }

    private List<Node> getChildNodesFromNodeList( NodeList nodeList, String nodeName ) {
        return getChildNodesFromNodeList( nodeList ).stream().filter( node -> node.getNodeName().equals( nodeName ) ).collect(Collectors.toList());
    }
}