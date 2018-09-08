code_1 = '''class Solution {    
    public void setZeroes(int[][] matrix) {
    }
}'''

code_2 = '''/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int kthSmallest(TreeNode root, int k) {
    
    }
}'''

pattern_1 = '''
/**
 * @author {author}
 * @date {date}
 */
public class Solution implements Answer {{
    @Override
    public {sign[ret]} {sign[name]}({sign[param]}) {{
        
    }}
}}
'''
'''package {en_level}.q{index:0>3s};'''
pattern_test=ad_test_class_pattern = '''

import com.rits.cloning.Cloner;
import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;

/**
 * @author {author}
 * @date {date}
 */
 
public class SolutionTest {{
    private static Cloner cloner;
    private static Answer[] answers;

    @BeforeClass
    public static void init() {{
        cloner = new Cloner();
        answers = new Answer[]{{new Solution()}};
    }}

    @Test
    public void test() {{
        // simpleCase: {case}
        {sign[param_1]} param = null;
        {sign[ret]} expect = null;
        testAnswer(param, expect);
    }}

    private void testAnswer({sign[param_1]} input, int expect) {{
        for (Answer answer : answers) {{
            {sign[param_1]} param = cloner.deepClone(input);
            {sign[ret]} result = answer.{sign[name]}(param);

            boolean correct = result == expect;
            if (!correct) {{
                String info = String.format("\\nAnswer: %s\\tExpect: %s\\tActual: %s",
                        answer.getClass().getSimpleName(), expect, result);
                Assert.fail(info);
            }}
        }}
    }}
}}
'''